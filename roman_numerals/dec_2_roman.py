from collections import OrderedDict

values = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
digits = OrderedDict(zip(keys[::-1], values[::-1]))


def dec2rom(i):
    res = ''
    while i > 0:
        for k in digits.keys():
            if i - k >= 0:
                max_value = k
                break
        i = i - max_value
        res += digits[max_value]
    return res

print(dec2rom(1996))