from collections import OrderedDict

values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
keys = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

digits = OrderedDict(zip(keys[::-1], values[::-1]))


def rom2dec(i):
    res = 0
    while i:
        for k in digits.keys():
            if i.startswith(k):
                max_value = k
                break
        i = i[len(k):]
        res += digits[max_value]
    return res

print(rom2dec("MMXII"))