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
    m=i_input()
    n = i_input()
    amap = [ l_input() for _ in range(n) ]
    return m,n,amap

def dfs(row, col, amap):
    count = 0
    n = len(amap)
    m = len(amap[0])
    for dr, dc in [ (-1, 0), (+1, 0), (0, -1), (0, +1) ]:
        if 0 <= row+dr < n and 0 <= col+dc < m and amap[row+dr][col+dc] == 1:
            amap[row+dr][col+dc] = 0
            tmp = 1 + dfs(row+dr, col+dc, amap)
            amap[row+dr][col+dc] = 1
            count = max(count, tmp)
    return count

def solve(m,n,amap):
    count = 0
    for row in range(n):
        for col in range(m):
            if amap[row][col] == 1:
                count = max(count, dfs(row, col, amap))
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    m,n,amap=readinput()
    ans=solve(m,n,amap)
    printans(ans)
