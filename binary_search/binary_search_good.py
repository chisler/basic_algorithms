def binary_search(array, element):
    start, end = 0, len(array) - 1

    while start <= end:
        middle = (start + end) // 2

        if element < array[middle]:
            end = middle - 1
        elif element > array[middle]:
            start = middle + 1
        if element == array[middle]:
            return middle
    return -1


array = [2, 3, 4, 1, 5]
array = sorted(array)

print(list(enumerate(array)))

for i in range(10):
    print(binary_search(array, i))