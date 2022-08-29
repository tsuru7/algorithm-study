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
    dmat = [[INFTY for i in range(n)] for j in range(n)]
    for i in range(n):
        dmat[i][i] = 0
    tmat = [[INFTY for i in range(n)] for j in range(n)]
    for i in range(n):
        tmat[i][i] = 0
    for _ in range(m):
        s, t, d, time = m_input()
        s -= 1
        t -= 1
        dmat[s][t] = d
        dmat[t][s] = d
        tmat[s][t] = time
        tmat[t][s] = time
    return n,m,dmat,tmat

def solve(n,m,dmat,tmat):
    dp = [[[INFTY, 0] for i in range(n)] for j in range(2**n)]
    dp[0][0] = [0, 1]
    for vstat in range(2**n):
        for s in range(n):
            for t in range(n):
                if s == t or vstat & 1<<t > 0:
                    continue
                etime = dp[vstat][s][0]
                dst = dmat[s][t]
                if tmat[s][t] < etime + dst:
                    continue
                if dp[vstat|1<<t][t][0] > etime + dst:
                    dp[vstat|1<<t][t][0] = etime + dst
                    dp[vstat|1<<t][t][1] = dp[vstat][s][1]
                elif dp[vstat|1<<t][t][0] == etime + dst:
                    dp[vstat|1<<t][t][1] += dp[vstat][s][1]
    # print(*dp, sep='\n')
    if dp[-1][0][0] == INFTY:
        ans = ['IMPOSSIBLE']
    else:
        ans = dp[-1][0]
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,m,dmat,tmat=readinput()
    ans=solve(n,m,dmat,tmat)
    printans(ans)
