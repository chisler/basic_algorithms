def sqrt(s, x=1):
    if abs(x * x - s) < 0.1 ** 3:
        return x

    x = 0.5 * (x + s/x)
    return sqrt(s, x)

print(sqrt(144))