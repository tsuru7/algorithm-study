import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
import random

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

def judge(s, budget, cmap, hmax, wmax):
    for w in range(1, wmax+1):
        if s % w != 0:
            continue
        h = s // w
        if h > hmax:
            continue
        for t in range(hmax-h+1):
            b = t + h 
            for l in range(wmax-w+1):
                r = l + w
                p = cmap[b][r] - cmap[b][l] - cmap[t][r] + cmap[t][l]
                if p <= budget:
                    return True
    return False

def solve(h,w,k,v,amap):
    cmap = [[0 for col in range(w+1)] for row in range(h+1)]
    for row in range(1, h+1):
        for col in range(1, w+1):
            cmap[row][col] = cmap[row][col-1] + amap[row-1][col-1]
    for col in range(1, w+1):
        for row in range(1, h+1):
            cmap[row][col] += cmap[row-1][col]
    # print(*cmap)
    suma = 0
    mina = INFTY
    for row in range(h):
        suma += sum(amap[row])
        mina = min(mina, min(amap[row]))
    if v >= h*w*k + suma:
        return h*w
    if v < k+mina:
        return 0
    # ここに来たとき、面積 1 なら OK 面積 H*W なら NG
    ac = 1
    wa = h*w
    print(f'ac: {ac}, wa: {wa}')
    while wa - ac > 1:
        wj = (ac+wa)//2
        if judge(wj, v - wj*k, cmap, h, w):
            ac = wj
        else:
            wa = wj
        print(f'ac: {ac}, wa: {wa}')
    return ac

def solve2(h,w,k,v,amap):
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
    shape = (0, 0, 0, 0)
    for t in range(1, h+1):
        for l in range(1, w+1):
            for b in range(t, h+1):
                for r in range(l, w+1):
                    area = (b-t+1)*(r-l+1)
                    parea = area * k
                    pland = cmap[b][r] + cmap[t-1][l-1] - cmap[b][l-1] - cmap[t-1][r]
                    if parea + pland <= v:
                        if amax < area:
                            amax = area
                            shape = (t,l, b,r)

    print(shape)
    return amax

def randinput():
    h, w = 4, 5
    k = 1
    v = 1000
    amap = [[random.randint(1, 100) for i in range(w)] for j in range(h)]
    return h,w,k,v,amap

def buginput():
    h, w = 4, 5
    k = 1
    v = 1000
    amap = [[25, 24, 97, 44, 28], [84, 97, 53, 56, 99], [90, 50, 92, 54, 100],[89, 35, 26, 50, 92]]
    # amap = [[random.randint(1, 100) for i in range(w)] for j in range(h)]
    return h,w,k,v,amap

def printans(ans):
    print(ans)

if __name__=='__main__':
    # h,w,k,v,amap=readinput()
    while True:
        # h,w,k,v,amap=randinput()
        h,w,k,v,amap=buginput()
        ans=solve(h,w,k,v,amap)
        ans2=solve2(h,w,k,v,amap)
        printans(ans)
        printans(ans2)
        if ans != ans2:
            print(*amap, sep='\n')
            break
