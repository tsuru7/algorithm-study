import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
import numpy as np

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    H,W,n,h,w=m_input()
    amat = [l_input() for _ in range(H)]
    return H,W,n,h,w,amat

def solve(H,W,n,h,w,amat):
    count = np.array([0 for _ in range(n+1)])
    cum2d = np.array([[[0 for _ in range(W+1)] for _ in range(H+1)] for _ in range(n+1)])
    for row in range(H):
        for col in range(W):
            aij = amat[row][col]
            count[aij] += 1
    # print(f'count: {count}')
    for row in range(1, H+1):
        for col in range(1, W+1):
            aij = amat[row-1][col-1]
            for num in range(1, n+1):
                if num == aij:
                    cum2d[num, row, col] = cum2d[num, row, col-1] + 1
                else:
                    cum2d[num, row, col] = cum2d[num, row, col-1]
    for col in range(1, W+1):
        for row in range(1, H+1):
            for num in range(1, n+1):
                cum2d[num, row, col] += cum2d[num, row-1, col]
    # for num in range(1, n+1):
    #     print(f'cum2d[num]: {cum2d[num][H][W]}')

    ans=[[0 for _ in range(W-w+1)] for _ in range(H-h+1)]
    for row in range(H-h+1):
        for col in range(W-w+1):
            l = col + 1
            r = l + w - 1
            u = row + 1
            d = u + h - 1
            # print(f'l: {l}, u: {u}, r: {r}, d: {d}')
            tmp = 0
            # for num in range(1, n+1):
            #     delcnt = cum2d[num, d, r] + cum2d[num, u-1, l-1] - cum2d[num, d, l-1] - cum2d[num, u-1, r]
            #     if count[num] - delcnt > 0:
            #         tmp += 1
            delcnt = cum2d[:, d, r] + cum2d[:, u-1, l-1] - cum2d[:, d, l-1] - cum2d[:, u-1, r]
            tmp = count - delcnt > 0 
            ans[row][col] = tmp.sum()
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    H,W,n,h,w,amat=readinput()
    ans=solve(H,W,n,h,w,amat)
    printans(ans)
