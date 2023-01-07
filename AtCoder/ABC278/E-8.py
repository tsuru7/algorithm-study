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
    H,W,n,h,w=m_input()
    amat = [l_input() for _ in range(H)]
    return H,W,n,h,w,amat

class Accumulate2d:
    def __init__(self, H, W, n, amat):
        self.cum2d = [[[0 for _ in range(W+1)] for _ in range(H+1)] for _ in range(n+1)]
        for num in range(1, n+1):
            for row in range(1, H+1):
                for col in range(1, W+1):
                    aij = amat[row-1][col-1]
                    self.cum2d[num][row][col] = self.cum2d[num][row][col-1]
                    if aij == num:
                        self.cum2d[num][row][col] += 1
            for col in range(W+1):
                for row in range(H+1):
                    self.cum2d[num][row][col] += self.cum2d[num][row-1][col]
    def rangeCount(self, num, u, l, d, r):
        return self.cum2d[num][d][r] + self.cum2d[num][u-1][l-1] \
             - self.cum2d[num][d][l-1] - self.cum2d[num][u-1][r]

class Accumulate2d_2:
    def __init__(self, H, W, n, amat):
        self.cum2d = [[[0 for _ in range(n+1)] for _ in range(W+1)] for _ in range(H+1)]
        for row in range(1, H+1):
            for col in range(1, W+1):
                aij = amat[row-1][col-1]
                for num in range(1, n+1):
                    self.cum2d[row][col][num] = self.cum2d[row][col-1][num]
                    if aij == num:
                        self.cum2d[row][col][num] += 1
        for col in range(W+1):
            for row in range(H+1):
                for num in range(1, n+1):
                    self.cum2d[row][col][num] += self.cum2d[row-1][col][num]
    def rangeCount(self, num, u, l, d, r):
        return self.cum2d[d][r][num] + self.cum2d[u-1][l-1][num] \
             - self.cum2d[d][l-1][num] - self.cum2d[u-1][r][num]

def solve(H,W,n,h,w,amat):
    count = [0 for _ in range(n+1)]
    cum2d = Accumulate2d_2(H, W, n, amat) 

    for row in range(H):
        for col in range(W):
            aij = amat[row][col]
            count[aij] += 1

    ans=[[0 for _ in range(W-w+1)] for _ in range(H-h+1)]
    for row in range(H-h+1):
        for col in range(W-w+1):
            for num in range(1, n+1):
                l = col + 1
                r = l + w - 1
                u = row + 1
                d = u + h - 1
                delcnt = cum2d.rangeCount(num,u,l,d,r)
                if count[num] - delcnt > 0:
                    ans[row][col] += 1
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    H,W,n,h,w,amat=readinput()
    ans=solve(H,W,n,h,w,amat)
    printans(ans)
