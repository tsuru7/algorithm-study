n = int(input())
a = list(map(int,input().split()))

flag=True
count=0
while flag:
    flag=False
    for j in range(n-1, 0, -1):
        if (a[j] < a[j-1]):
            (a[j-1], a[j]) = (a[j], a[j-1])
            flag=True
            count += 1
print(' '.join(map(str,a)))
print(count)
