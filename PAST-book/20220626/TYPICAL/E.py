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
    n,m=m_input()
    dist = [ [INFTY for i in range(n)] for j in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        u, v, c = m_input()
        dist[u][v] = c
    return n,m,dist

def solve(n,m,dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    # print()
    # for i in range(n):
    #     print(*dist[i])
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += dist[i][j]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,dist=readinput()
    ans=solve(n,m,dist)
    printans(ans)
