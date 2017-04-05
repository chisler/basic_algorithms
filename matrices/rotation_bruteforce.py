def get_row(a, row_number):
    return a[row_number]


def get_column(a, column_number):
    return [row[column_number] for row in a]


def is_squared(a):
    l = len(a)
    return all([(len(row) == l) for row in a])


def rotated_matrix(a):
    if not is_squared(a):
        raise ValueError("Not squared matrix")

    rotated = []
    for column in range(len(a)):
        rotated.append(list(reversed(get_column(a, column))))

    return rotated

a = [[1, 2, 3],
     [3, 4, 3],
     [5, 6, 7]]

print(rotated_matrix(a))