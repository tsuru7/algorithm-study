n=int(input())
aList = []
bList = []
for _ in range(n):
    a, b = map(int, input().split())
    aList.append(a)
    bList.append(b)

npush = 0
for i in range(n-1, -1, -1):
    # print(i)
    a = aList[i]
    b = bList[i]
    r = (a + npush) % b
    if r != 0:
        npush += b - r
    # print(f'npush: {npush}')

print(npush)

