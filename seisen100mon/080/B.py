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
    h,w,k,v=m_input()
    amap = [l_input() for _ in range(h)]
    return h,w,k,v,amap

def solve(h,w,k,v,amap):
    cmap = [[0 for j in range(w+1)] for i in range(h+1)]
    for row in range(h):
        for col in range(w):
            cmap[row+1][col+1] = cmap[row+1][col] + amap[row][col]
    for col in range(w):
        for row in range(h):
            cmap[row+1][col+1] += cmap[row][col+1]
    asum = 0
    amin = INFTY
    for row in range(h):
        asum += sum(amap[row])
        amin = min(amin, min(amap[row]))
    if v < k+amin:
        return 0
    if v >= h*w*k + asum:
        return h*w
    amax = 0
    for t in range(1, h+1):
        for l in range(1, w+1):
            for b in range(t, h+1):
                for r in range(l, w+1):
                    area = (b-t+1)*(r-l+1)
                    parea = area * k
                    pland = cmap[b][r] + cmap[t-1][l-1] - cmap[b][l-1] - cmap[t-1][r]
                    if parea + pland <= v:
                        amax = max(amax, area)

    return amax

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,k,v,amap=readinput()
    ans=solve(h,w,k,v,amap)
    printans(ans)
