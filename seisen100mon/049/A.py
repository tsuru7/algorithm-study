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
    dmat = [[INFTY for i in range(n)] for j in range(n)]
    for i in range(n):
        dmat[i][i] = 0
    for _ in range(m):
        s, t, d = m_input()
        dmat[s][t] = d
    return n,m,dmat

def solve(n,m,dmat):
    dp = [[INFTY for i in range(n)] for j in range(2**n)]
    # print(f'n: {n}, 2**n: {2**n}')
    dp[0][0] = 0
    for vstate in range(2**n):
        for i in range(n):
            for j in range(n):
                if i == j or vstate & 1<<j > 0:
                    continue
                # print(f'vstate: {vstate}, j: {j}, vstate|1<<j: {vstate|1<<j}')
                dp[vstate|1<<j][j] = min(dp[vstate|1<<j][j], dp[vstate][i] + dmat[i][j])

    if dp[-1][0] < INFTY:
        ans = dp[-1][0]
    else:
        ans = -1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,dmat=readinput()
    ans=solve(n,m,dmat)
    printans(ans)
