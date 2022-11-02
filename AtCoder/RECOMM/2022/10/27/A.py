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
    n,m,k,s,t,x=m_input()
    s -= 1
    t -= 1
    x -= 1
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,m,k,s,t,x,graph

def solve(n,m,k,s,t,x,graph):
    MOD = 998244353
    dpe = [[0 for _ in range(n)] for _ in range(k+1)]
    dpo = [[0 for _ in range(n)] for _ in range(k+1)]
    dpe[0][s] = 1
    for i in range(k):
        for j in range(n):
            for v in graph[j]:
                if v != x:
                    dpe[i+1][v] += dpe[i][j]
                    dpo[i+1][v] += dpo[i][j]
                else:
                    dpo[i+1][v] += dpe[i][j]
                    dpe[i+1][v] += dpo[i][j]
                dpe[i+1][v] %= MOD
                dpo[i+1][v] %= MOD

    return dpe[k][t]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,s,t,x,graph=readinput()
    ans=solve(n,m,k,s,t,x,graph)
    printans(ans)
