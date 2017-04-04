# Binary search looks up for an element in a sorted array
# This one copies array and do not return the index. It's a bad one:


def left_side(array):
    return array[:len(array) // 2]


def right_side(array):
    return array[len(array) // 2:]


def middle(array):
    if len(array) % 2 == 0:
        return (array[(len(array) // 2) - 1] + array[len(array) // 2]) / 2
    return array[len(array) // 2]


def binary_search(array, element):
    if len(array) == 1:
        return array[0] == element

    m = middle(array)
    if element < m:
        return binary_search(left_side(array), element)
    elif element > m:
        return binary_search(right_side(array), element)
    return m == element


array = [2, 3, 4, 1, 5]
array = sorted(array)

for i in range(10):
    print(binary_search(array, i))
