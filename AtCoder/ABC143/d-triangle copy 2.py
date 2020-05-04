from bisect import bisect_right

n = int(input())
l = list(map(int,input().split()))
l.sort() # 昇順にソート

count = 0
for i in range(0,n-2):
    a = l[i]
    for j in range(i+1, n-1):
        ab = a+l[j]
        # bisect_left(a, x): x を a に挿入できる点を返す
        # cの最大値は a+b-1
        k = bisect_right(l, ab-1, j+1, n)
        count += k-(j+1)
print(count)
