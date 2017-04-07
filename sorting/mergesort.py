def merge(a, b):
    i, j, res = 0, 0, []

    len_a, len_b = len(a) , len(b)

    while i < len_a or j < len_b:

        if i < len_a and (j >= len_b or a[i] < b[j]):
            res.append(a[i])
            i += 1
        elif j < len_b:
            res.append(b[j])
            j += 1

    return res


def sort(array):
    l = len(array)

    if l == 1:
        return array

    return list(merge(sort(array[:l//2]), sort(array[l//2:])))


print(sort([3, 2,1, 4, -2]))