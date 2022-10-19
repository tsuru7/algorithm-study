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
    h,w,n=m_input()
    snow = [l_input() for _ in range(n)]
    return h,w,n,snow

def solve(h,w,n,snow):
    land = [[0 for _ in range(w+2)] for _ in range(h+2)]
    for a, b, c, d in snow:
        land[a][b] += 1
        land[a][d+1] -= 1
        land[c+1][b] -= 1
        land[c+1][d+1] += 1
    for row in range(1, h+1):
        for col in range(1, w+1):
            land[row][col] += land[row][col-1]
    for col in range(1, w+1):
        for row in range(1, h+1):
            land[row][col] += land[row-1][col]
    
    return land

def printans(ans):
    h = len(ans)-2
    for row in range(h):
        print(*ans[row+1][1:-1])

if __name__=='__main__':
    h,w,n,snow=readinput()
    ans=solve(h,w,n,snow)
    printans(ans)
