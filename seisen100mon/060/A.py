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
    n, m = m_input()
    dist = [ [INFTY for i in range(n)] for j in range(n) ]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        s, t, d = m_input()
        dist[s][t] = d
    return n,m,dist

def solve(n,m,dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] == INFTY or dist[k][j] == INFTY:
                    continue
                else:
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    ans = []
    for i in range(n):
        if dist[i][i] < 0:
            ans = ['NEGATIVE CYCLE']
            break
        tmp = []
        for j in range(n):
            tmp.append(str(dist[i][j]) if dist[i][j] != INFTY else 'INF')
        ans.append(' '.join(tmp))
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,m,dist=readinput()
    ans=solve(n,m,dist)
    printans(ans)
