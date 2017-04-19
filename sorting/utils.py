from random import randint


def rand_array():
    length = randint(1, 10)

    return list([randint(-10000, 10000) for _ in range(length)])


def test_sorting(sorting_function):
    for array in [rand_array() for _ in range(100)]:
        assert sorted(array) == sorting_function(array)