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
    n=i_input()
    points = [l_input() for _ in range(n)]
    return n,points

def judge(s, points, smat):
    d = [ [False for i in range(n)] for j in range(n) ]
    for i in range(n):
        for j in range(n):
            d[i][j] = s >= smat[i][j]
    for k in range(n):
        for i in range(n):
            dik = d[i][k]
            for j in range(n):
                d[i][j] |= dik & d[k][j]
    for i in range(n):
        ans = True
        for j in range(n):
            ans &= d[i][j]
        if ans:
            return True
    return False

def solve(n,points):
    smat = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        xi, yi, pi = points[i]
        for j in range(n):
            xj, yj, pj = points[j]
            dist = abs(xi-xj)+abs(yi-yj)
            smat[i][j] = (dist + pi -1)//pi
    wa = 0
    ac = 10**10
    while ac - wa > 1:
        wj = (ac+wa)//2
        # print(f'wa: {wa}, wj: {wj}, ac: {ac}')
        if judge(wj, points, smat):
            ac = wj
        else:
            wa = wj
    
    return ac

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,points=readinput()
    ans=solve(n,points)
    printans(ans)
