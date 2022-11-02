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
    ans = 0
    points = []
    for row in range(9):
        for col in range(9):
            if smap[row][col] == '#':
                points.append((row, col))
    npoints = len(points)
    points_set = set(points)
    for i1 in range(npoints):
        x1, y1 = points[i1]
        for i2 in range(npoints):
            if i2 == i1:
                continue
            x2, y2 = points[i2]
            ux = x2 - x1
            uy = y2 - y1
            if ux < 0 or uy >= 0:
                continue
            vx = uy
            vy = -ux
            x3 = x2 + vx
            y3 = y2 + vy
            if (x3, y3) not in points_set:
                continue
            x4 = x3 - ux
            y4 = y3 - uy
            if (x4, y4) in points_set:
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    smap=readinput()
    ans=solve(smap)
    printans(ans)
