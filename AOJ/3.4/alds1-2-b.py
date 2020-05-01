n = int(input())
a = list(map(int,input().split()))

count = 0
for i in range(n):
    minj = i
    for j in range(i, n):
        if (a[j]<a[minj]):
            minj = j
    if (minj != i):
        (a[i], a[minj]) = (a[minj], a[i])
        count += 1

print(' '.join(map(str,a)))
print(count)
