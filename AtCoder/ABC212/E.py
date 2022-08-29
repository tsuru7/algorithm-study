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
    nnList = []
    for _ in range(n):
        nList.append([])
        nnList.append([])
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        nList[u].append(v)
        nList[v].append(u)
    for i in range(n):
        for j in range(n):
            if i == j or j in nList[i]:
                continue
            nnList[i].append(j)
    return n,m,k,nnList

def main(n,m,k,nList):
    MOD = 998244353
    dp = [ [0]*n for _ in range(k+1)]
    # print(dp)
    dp[0][0] = 1
    for day in range(1, k+1):
        for town in range(n):
            for town0 in nList[town]:
                if town0 == town:
                    continue
                # print(f'day: {day}, town: {town}, town0: {town0}')
                dp[day][town] += dp[day-1][town0]
                dp[day][town] = dp[day][town] % MOD
    ans=dp[k][0]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,k,nList=readinput()
    ans=main(n,m,k,nList)
    printans(ans)
