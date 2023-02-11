
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

H,W,n,h,w=m_input()
amat = [l_input() for _ in range(H)]

count = [0 for _ in range(n+1)]
cum2d = [0 for _ in range((W+1)*(H+1)*(n+1))]
to1d = lambda num, row, col: num*(H+1)*(W+1) + row*(W+1) + col

for row in range(H):
    for col in range(W):
        aij = amat[row][col]
        count[aij] += 1
for num in range(1, n+1):
    for row in range(1, H+1):
        for col in range(1, W+1):
            cum2d[to1d(num, row, col)] = cum2d[to1d(num, row-1, col)] + cum2d[to1d(num, row, col-1)] - cum2d[to1d(num, row-1, col-1)]
            aij = amat[row-1][col-1]
            if num == aij:
                cum2d[to1d(num,row,col)] += 1

ans=[[0 for _ in range(W-w+1)] for _ in range(H-h+1)]
for num in range(1, n+1):
    for row in range(H-h+1):
        for col in range(W-w+1):
            l = col + 1
            r = l + w - 1
            u = row + 1
            d = u + h - 1
            delcnt = cum2d[to1d(num,d,r)] + cum2d[to1d(num,u-1,l-1)] - cum2d[to1d(num,d,l-1)] - cum2d[to1d(num,u-1,r)]
            if count[num] - delcnt > 0:
                ans[row][col] += 1
for a in ans:
    print(*a)
