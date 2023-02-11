import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    smap = [input() for _ in range(h)]
    return h,w,smap

def solve(h,w,smap):
    yoko = [[-1] for _ in range(h)]
    tate = [[-1] for _ in range(w)]
    for row in range(h):
        for col in range(w):
            if smap[row][col] == '#':
                yoko[row].append(col)
        yoko[row].append(w)
    for col in range(w):
        for row in range(h):
            if smap[row][col] == '#':
                tate[col].append(row)
        tate[col].append(h)
    # print(*yoko, sep='\n')
    # print(*tate, sep='\n')
    ans=0
    for row in range(h):
        for col in range(w):
            if smap[row][col] == '#':
                continue
            idx_yoko = bisect_left(yoko[row], col)
            l = yoko[row][idx_yoko-1]
            r = yoko[row][idx_yoko]

            idx_tate = bisect_left(tate[col], row)
            u = tate[col][idx_tate-1]
            d = tate[col][idx_tate]
            ans = max(ans, r-1-l + d-1-u - 1)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,smap=readinput()
    ans=solve(h,w,smap)
    printans(ans)
