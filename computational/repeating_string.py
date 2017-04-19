def replace_repeated(s):
    res = ''
    cur = ''
    cnt = 0
    last = ''

    for c in s:
        if cur != c:
            cur = c
            if cnt:
                res += str(cnt) + last
            cnt = 0
        cnt += 1
        last = c

    if cnt:
        res += str(cnt) + last

    return res


print(replace_repeated('aaaabbsssbhhh'))
