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
    for x1 in range(9):
        for y1 in range(9):
            if smap[x1][y1] == '.':
                continue
            for x2 in range(9):
                for y2 in range(9):
                    if smap[x2][y2] == '.':
                        continue
                    if x2 == x1 and y2 == y1:
                        continue
                    ux = x2 - x1
                    uy = y2 - y1
                    # if ux < 0 or uy >= 0:
                    #     continue

                    vx = -uy
                    vy = ux
                    x3 = x2 + vx
                    y3 = y2 + vy
                    if not (0 <= x3 < 9 and 0 <= y3 < 9):
                        continue
                    if smap[x3][y3] == '.':
                        continue
                    x4 = x3 - ux
                    y4 = y3 - uy
                    if not (0 <= x4 < 9 and 0 <= y4 < 9):
                        continue
                    if smap[x4][y4] == '.':
                        continue
                    ans += 1
                    # print((x1, y1), (x2, y2), (x3,y3), (x4, y4))
    return ans//4

def printans(ans):
    print(ans)

if __name__=='__main__':
    smap=readinput()
    ans=solve(smap)
    printans(ans)
