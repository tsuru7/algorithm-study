n = int(input())
l = list(map(int,input().split()))
l.sort() # 昇順にソート

count = 0
for i in range(0,n-2):
    a = l[i]
    for j in range(i+1, n-1):
        ab = a+l[j]
        # バイナリサーチでl[k] < a+b  となる最小のkを探す
        # j+1, ..., k で三角形ができる k-j 個
        left = j+1
        right = n
        while (left < right):
            middle = (left + right) // 2
            #print('left: {} middle:{} right: {}'.format(left, middle, right))
            c = l[middle]
            if (c < ab):
                left = middle+1 #  l[left-1]は三角形が作れる
            elif( ab <= c):
                right = middle  #  l[right] は三角形が作れない
        # left-1 が argmin_k(a+b>l[k])
        count += left-1 - j
print(count)
