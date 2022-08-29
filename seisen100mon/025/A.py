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
    amaps = []
    w, h = m_input()
    while not (w == 0 and h == 0):
        tmp = [ l_input() for _ in range(h) ]
        amaps.append(tmp)
        w, h = m_input()
    return amaps

def rc2ind(row, col, h, w):
    return row*w+col

def ind2rc(ind, h, w):
    return divmod(ind, w)

def dfs(ind, amap, visited):
    visited[ind] = True
    h = len(amap)
    w = len(amap[0])
    row, col = ind2rc(ind, h, w)
    for dr, dc in [ (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1) ]:
        if 0 <= row+dr < h and 0 <= col+dc < w and amap[row+dr][col+dc] == 1:
            newind = rc2ind(row+dr, col+dc, h, w)
            if visited[newind]:
                continue
            dfs(newind, amap, visited)


def solve(amaps):
    ans=[]
    for amap in amaps:
        h = len(amap)
        w = len(amap[0])
        visited = [False]*(h*w)
        count = 0
        for ind in range(h*w):
            if visited[ind]:
                continue
            row, col = ind2rc(ind, h, w)
            if amap[row][col] == 0:
                continue
            count += 1
            dfs(ind, amap, visited)
        ans.append(count)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    amap=readinput()
    ans=solve(amap)
    printans(ans)
