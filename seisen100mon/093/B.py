import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from copy import deepcopy

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
    h,w,k=m_input()
    cmap = [list(map(int, list(input()))) for _ in range(h)]
    return h,w,k,cmap

def dropstones(cmap):
    h = len(cmap)
    w = len(cmap[0])
    for col in range(w):
        zeros = 0
        for row in range(h)[::-1]:
            if cmap[row][col] == 0:
                zeros += 1
            else:
                cmap[row+zeros][col] = cmap[row][col]
                cmap[row][col] = 0

def play(cmap, k):
    ans = 0
    dropstones(cmap)
    point = erasestones(cmap, k)
    while point > 0:
        ans += point
        dropstones(cmap)
        point = erasestones(cmap, k)
    return ans

def solve(h,w,k,cmap):
    ans=0
    for row in range(h):
        for col in range(w):
            tmp = deepcopy(cmap)
            tmp[row][col] = 0
            ans = max(ans, play(tmp, k)) 
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,k,cmap=readinput()
    ans=solve(h,w,k,cmap)
    printans(ans)
