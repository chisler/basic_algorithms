from random import randint

from sorting.utils import test_sorting


def partition(array, start, end):
    pivot = array[randint(start, end)]

    while start < end:
        while array[start] < pivot and start < end:
            start += 1

        while array[end] > pivot and start < end:
            end -= 1

        array[start], array[end] = array[end], array[start]

    return array, start


def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start >= end:
        return array

    array, p = partition(array, start, end)

    quicksort(array, start, p - 1)
    quicksort(array, p + 1, end)

    return array


test_sorting(quicksort)
