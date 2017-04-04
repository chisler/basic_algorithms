def left_indexes(start, end):
    return start, (end - start) // 2


def right_indexes(start, end):
    return (end - start) // 2, end


def middle(array, start, end):
    length = end - start + 1

    if length % 2 == 0:
        return (array[length // 2 - 1] + array[length // 2]) / 2, False
    return array[length // 2], True


def binary_search(array, element, start=0, end=None):
    if end is None:
        end = len(array)

    if end - start < 1:
        return start if array[start] == element else -1

    mid, present = middle(array, start, end)

    if element < mid:
        return binary_search(array, element, *left_indexes(start, end))
    elif element > mid:
        return binary_search(array, element, *right_indexes(start, end))

    if element == mid:
        return array[(end - start) // 2] if present else -1


array = [2, 3, 4, 1, 5]
array = sorted(array)

for i in range(10):
    print(binary_search(array, i))

