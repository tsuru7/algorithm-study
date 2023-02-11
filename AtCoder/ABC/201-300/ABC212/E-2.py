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
    n,m,k=m_input()
    nList = []
    for i in range(n):
        nList.append([i])
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        nList[u].append(v)
        nList[v].append(u)
    return n,m,k,nList

def main(n,m,k,nList):
    MOD = 998244353
    dp = [ [0]*n for _ in range(k+1) ]
    dp[0][0] = 1
    pre = 1
    for day in range(1, k+1):
        pre = sum(dp[day-1]) % MOD
        for town in range(n):
            dp[day][town] = pre
            for town0 in nList[town]:
                dp[day][town] -= dp[day-1][town0]
            dp[day][town] = dp[day][town] % MOD
            # now += dp[day][town]
        # now = now % MOD
        # pre = now
        
    ans=dp[k][0] % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,nList=readinput()
    ans=main(n,m,k,nList)
    printans(ans)
