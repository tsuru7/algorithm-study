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
    gmap = [input() for _ in range(h)]
    return h,w,gmap

def canmove(row, col, gmap):
    h = len(gmap)
    w = len(gmap[0])
    dir = gmap[row][col]
    if dir == 'U' and row == 0:
        return False
    if dir == 'D' and row == h-1:
        return False
    if dir == 'L' and col == 0:
        return False
    if dir == 'R' and col == w-1:
        return False
    return True

def solve(h,w,gmap):
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[0][0] = True
    row = 0
    col = 0
    while canmove(row, col, gmap):
        dir = gmap[row][col]
        if dir == 'U':
            row -= 1
        elif dir == 'D':
            row += 1
        elif dir == 'L':
            col -= 1
        elif dir == 'R':
            col += 1
        if visited[row][col]:
            return [-1]
        visited[row][col] = True
    return [row+1, col+1]

    ans=0
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    h,w,gmap=readinput()
    ans=solve(h,w,gmap)
    printans(ans)
