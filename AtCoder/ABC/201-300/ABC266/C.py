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
    points = [l_input() for _ in range(4)]
    return points

def gaiseki(ax, ay, bx, by):
    return ax*by - ay*bx


def solve(points):
    for i in range(4):
        p0x, p0y = points[i]
        p1x, p1y = points[(i+1)%4]
        p2x, p2y = points[(i-1)%4]
        v1x = p1x - p0x
        v1y = p1y - p0y
        v2x = p2x - p0x
        v2y = p2y - p0y
        if gaiseki(v1x, v1y, v2x, v2y) < 0:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    points=readinput()
    ans=solve(points)
    printans(ans)
