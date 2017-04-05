
def is_squared(a):
    l = len(a)
    return all([(len(row) == l) for row in a])


def rotated_matrix(a):
    if not is_squared(a):
        raise ValueError("Not squared matrix")

    return list(map(lambda x: list(reversed(x)), zip(*a)))

a = [[1, 2],
     [3, 4]]

print(rotated_matrix(a))