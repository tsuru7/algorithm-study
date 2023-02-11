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

def solve(n,points):
    smat = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        xi, yi, pi = points[i]
        for j in range(n):
            xj, yj, pj = points[j]
            dist = abs(xi-xj)+abs(yi-yj)
            smat[i][j] = (dist + pi -1)//pi
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                smat[i][j] = min(smat[i][j], max(smat[i][k], smat[k][j]))
    ans = INFTY
    for i in range(n):
        ans = min(ans, max(smat[i]))

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,points=readinput()
    ans=solve(n,points)
    printans(ans)
