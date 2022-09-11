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
    h,w=m_input()
    cmap = [ input() for _ in range(h) ]
    return h, w, cmap

cmap = None
visited = None
def dfs(u, goal):
    global visited

    row, col = u
    if u == goal:
        return True

    visited[row][col] = True
    for dr, dc in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
        if 0 <= row+dr <= h-1 and 0 <= col+dc <= w-1:
            if visited[row+dr][col+dc]:
                continue
            if cmap[row+dr][col+dc] == '#':
                continue
            v = (row+dr, col+dc)
            if dfs(v, goal):
                return True
    return False


def solve(h, w):
    global visited

    for row in range(h):
        for col in range(w):
            if cmap[row][col] == 's':
                start = (row, col)
            elif cmap[row][col] == 'g':
                goal = (row, col)
    visited = [ [False]*w for _ in range(h) ]
    u = start
    if dfs(u, goal):
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    h, w, cmap=readinput()
    ans=solve(h, w)
    printans(ans)
