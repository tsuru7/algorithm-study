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
    graph = [ [] for _ in range(n) ]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,m,k,s,t,x,graph

def solve(n,m,k,s,t,x,graph):
    MOD = 998244353
    dp = [ [ [0,0] for i in range(n) ] for j in range(k+1) ]
    s -= 1
    t -= 1
    x -= 1
    dp[0][s] = [1, 0]  # [偶数回(0も含む), 奇数回]
    for i in range(k):
        for j in range(n):
            for v in graph[j]:
                if v != x:
                    dp[i+1][v][0] += dp[i][j][0]
                    dp[i+1][v][1] += dp[i][j][1]
                else:
                    dp[i+1][v][0] += dp[i][j][1]
                    dp[i+1][v][1] += dp[i][j][0]
                dp[i+1][v][0] %= MOD
                dp[i+1][v][1] %= MOD

    ans=dp[k][t][0]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,s,t,x,graph=readinput()
    ans=solve(n,m,k,s,t,x,graph)
    printans(ans)
