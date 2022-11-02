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
    smap = [input() for _ in range(9)]
    return smap

def solve(smap):
    points = set()
    for x in range(9):
        for y in range(9):
            if smap[x][y] == '#':
                points.add((x, y))
    npoints = len(points)
    ans=0
    for x1, y1 in points:
        for x2, y2 in points:
            if (x1, y1) == (x2, y2):
                continue
            ux = x2 - x1
            uy = y2 - y1
            vx = -uy
            vy = ux
            x3 = x2 + vx
            y3 = y2 + vy
            if (x3, y3) not in points:
                continue
            x4 = x3 - ux
            y4 = y3 - uy
            if (x4, y4) not in points:
                continue
            ans += 1
    return ans // 4

def printans(ans):
    print(ans)

if __name__=='__main__':
    smap=readinput()
    ans=solve(smap)
    printans(ans)
