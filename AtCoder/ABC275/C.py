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
    ans_set = set()
    for i1 in range(npoints):
        x1, y1 = points[i1]
        for i2 in range(i1+1, npoints):
            x2, y2 = points[i2]
            for i3 in range(i2+1, npoints):
                x3, y3 = points[i3]
                ux = x2-x1
                uy = y2-y1
                vx = x3-x2
                vy = y3-y2
                if ux*vx + uy*vy != 0:
                    continue
                if ux*ux + uy*uy != vx*vx + vy*vy:
                    continue
                x4 = x3 - ux
                y4 = y3 - uy
                if (x4, y4) in points_set:
                    if (x1, y1, x2, y2, x3, y3, x4, y4) not in ans_set:
                        ans += 1
                    ans_set.add((x1, y1, x2, y2, x3, y3, x4, y4))
                    ans_set.add((x1, y1, x4, y4, x3, y3, x2, y2))
                    ans_set.add((x2, y2, x3, y3, x4, y4, x1, y1))
                    ans_set.add((x4, y4, x3, y3, x2, y2, x1, y1))
                    ans_set.add((x3, y3, x4, y4, x1, y1, x2, y2))
                    ans_set.add((x3, y3, x2, y2, x1, y1, x4, y4))
                    ans_set.add((x4, y4, x1, y1, x2, y2, x3, y3))
                    ans_set.add((y3, x2, y2, x1, y1, x4, y4, x3))
                    # print(points[i1], points[i2], points[i3], (x4, y4))
    # print(ans_set)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    smap=readinput()
    ans=solve(smap)
    printans(ans)
