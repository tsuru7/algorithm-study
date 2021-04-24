import numpy as np

m, n = map(int, input().split())
k = int(input())

accJmap = [[0]*(n+1) for i in range(m+1)]
accOmap = [[0]*(n+1) for i in range(m+1)]
# accJmap = np.zeros((m+1, n+1), dtype=int)
# accOmap = np.zeros((m+1, n+1), dtype=int)

for i in range(m):
    landLine = input()

    jcount = 0
    ocount = 0
    for idx, ch in enumerate(landLine):
        if ch == 'J':
            jcount += 1
        elif ch == 'O':
            ocount += 1
        accJmap[i+1][idx+1] = accJmap[i][idx+1] + jcount
        accOmap[i+1][idx+1] = accOmap[i][idx+1] + ocount
        # accJmap[i+1, idx+1] = accJmap[i, idx+1] + jcount
        # accOmap[i+1, idx+1] = accOmap[i, idx+1] + ocount

# print('Jmap')
# for i in range(m+1):
#     print(accJmap[i])

# print('Omap')
# for i in range(m+1):
#     print(accOmap[i])


for _ in range(k):
    a, b, c, d = map(int, input().split())
    jcount = accJmap[c][d] - accJmap[a-1][d] - accJmap[c][b-1] + accJmap[a-1][b-1]
    ocount = accOmap[c][d] - accOmap[a-1][d] - accOmap[c][b-1] + accOmap[a-1][b-1]
    icount = (c-a+1)*(d-b+1)-jcount-ocount
    print(f'{jcount} {ocount} {icount}')
