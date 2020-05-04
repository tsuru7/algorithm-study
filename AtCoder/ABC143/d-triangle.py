n = int(input())
l = []
l[:] = map(int,input().split())
l.sort()

c = 0
for i in range(0,n-2):
    a = l[i]
    for j in range(i+1, n-1):
        ab = a+l[j]
        k=n-1
        while (k>=j+1):
            if(ab<=l[k]):
                k-=1
            else:
                break
        c+=(k-j)
print(c)
