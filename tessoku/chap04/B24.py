import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left

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
    n=i_input()
    xyList = [l_input() for _ in range(n)]
    return n,xyList

def solve(n,xyList):
    dpx = [INFTY for _ in range(n)]
    dpy = [INFTY for _ in range(n)]
    xyList.sort()
    ans = 0
    for i in range(n):
        yi = xyList[i][1]
        idx = bisect_left(dpy, yi)
        # dpy[idx] = yi
        if idx == 0 or dpx[idx-1] < xyList[i][0]:
            dpx[idx] = xyList[i][0]
            dpy[idx] = xyList[i][1]
        else:
            continue
        ans = max(ans, idx+1)
    return ans

def solve2(n, xyList):
    ALL = 2**n
    ans = 0
    for x in range(1, ALL):
        selected = []
        for i in range(n):
            if x & (1<<i) > 0:
                selected.append(xyList[i])
        selected.sort()
        xi, yi = selected[0]
        flag = True
        for j in range(1, len(selected)):
            xj, yj = selected[j]
            if not (xi < xj and yi < yj):
                flag = False
            xi, yi = xj, yj
        if flag:
            ans = max(ans, len(selected))
    return ans

def randinput():
    import random
    n = 4
    xyList = [[random.randint(1, 20), random.randint(1, 20)] for _ in range(n)]
    return n, xyList

def printans(ans):
    print(ans)

if __name__=='__main__':
    while True:
        n,xyList=randinput()
        ans1=solve(n,xyList)
        ans2=solve2(n,xyList)
        if ans1 != ans2:
            print(ans1, ans2)
            print(xyList)
            break
        print(ans1, ans2)
