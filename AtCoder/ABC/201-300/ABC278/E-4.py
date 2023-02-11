import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    H,W,N,h,w=m_input()
    amat = [l_input() for _ in range(H)]
    return H,W,N,h,w,amat

def solve(H,W,N,h,w,amat):
    cum2d = [[0 for _ in range(W+1)] for _ in range(H+1)]
    ans=[[0 for _ in range(W-w+1)] for _ in range(H-h+1)]
    for num in range(1, N+1):
        for row in range(1, H+1):
            for col in range(1, W+1):
                cum2d[row][col] = cum2d[row][col-1] + cum2d[row-1][col] - cum2d[row-1][col-1]
                if amat[row-1][col-1] == num:
                    cum2d[row][col] += 1
        for row in range(H-h+1):
            for col in range(W-w+1):
                l = col + 1
                r = l + w - 1
                u = row + 1
                d = u + h - 1
                if cum2d[H][W] != cum2d[d][r] + cum2d[u-1][l-1] - cum2d[d][l-1] - cum2d[u-1][r]:
                    ans[row][col] += 1

    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    H,W,N,h,w,amat=readinput()
    ans=solve(H,W,N,h,w,amat)
    printans(ans)
