def is_even(i):
    return i % 2 == 0


# [1, 2, 3, 4, 5] -> 0, 1     | l = 4
# [1, 2, 3, 4, 5, 6] -> 0, 2  | l = 5
def left_indexes(start, end):
    l = end - start
    return start, start + (l - 1) // 2


# [1, 2, 3, 4, 5] -> 3, 4     | l = 4
# [1, 2, 3, 4, 5, 6] -> 3, 5  | l = 5
def right_indexes(start, end):
    l = end - start
    return start + l // 2 + 1, end


def middle(array, start, end):
    l = end - start

    if not is_even(l):
        return (array[start + l // 2] + array[start + l // 2] + 1) / 2, False
    return array[start + l // 2], True


def binary_search(array, element, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return start if array[start] == element else -1

    mid, present = middle(array, start, end)

    if element < mid:
        return binary_search(array, element, *left_indexes(start, end))

    if element > mid:
        return binary_search(array, element, *right_indexes(start, end))

    if element == mid:
        return (end - start) // 2 if present else -1


array = [2, 3, 4, 1, 5]
array = sorted(array)

print(list(enumerate(array)))

for i in range(10):
    print(binary_search(array, i))