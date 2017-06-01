def decrypt(code):
    z = {0: ' '}
    sum = 0
    res = ''
    arr = []
    for i in range(1, 27):
        z[i] = chr(i + 96)
    codes = code.split()
    for c in codes:
        for a in c:
            if a.isdigit():
                sum += int(a)
        if sum > 26:
            sum = sum % 27
        arr.append(sum)
        sum = 0
    for r in arr:
        res += z[r]
    return res


h = decrypt('x20*6<xY y875_r97L')
print(h)
