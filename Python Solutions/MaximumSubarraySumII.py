def find_subarr_maxsum(arr):
    sum = 0
    max = 0
    r = 0
    kek = -1
    ans = []
    pref = []
    for i in range(len(arr)):
        sum += arr[i]
        # print "{}. sum-{} max-{} \n".format(i, sum, max)
        if sum == max:
            l = kek + 1
            r = i
            ans.append(arr[l:r + 1])
            pref.append((l, r + 1))
        if sum > max:
            max = sum
            l = kek + 1
            r = i
            ans = [arr[l:r + 1]]
            pref = [(l, r + 1)]
        if sum < 0:
            sum = 0
            kek = i

    for i in pref:
        sum = 0
        kek = True
        for j in range(i[0], i[1]):
            if arr[j] == 0 and kek:
                if arr[j + 1:i[1]] not in ans:
                    ans.append(arr[j + 1:i[1]])
                continue
            kek = False
            sum += arr[j]
            if sum == 0:
                if arr[j + 1:i[1]] not in ans:
                    ans.append(arr[j + 1:i[1]])
    if len(ans) == 1:
        ans = ans[0]
    print([ans, max])
    return [[], 0] if max == 0 else [ans, max]


if __name__ == '__main__':
    arr = [4, -1, 2, 1, -40, 1, 2, -1, 4]
    (find_subarr_maxsum(arr))
