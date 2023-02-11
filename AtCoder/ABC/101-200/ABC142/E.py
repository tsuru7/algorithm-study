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
    abcList = []
    for _ in range(m):
        a, b = m_input()
        c = l_input()
        abcList.append((a, b, c))
    return n,m,abcList

def solve(n,m,abcList):
    ALL = 2**n
    dp = [[INFTY for _ in range(ALL)] for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(m):
        ai, bi, ci = abcList[i]
        bit = 0
        for b in ci:
            bit |= 1<<(b-1)
        # print(f'bit: {bit}, {bin(bit)}')
        for j in range(ALL):
            dp[i+1][j | bit] = min(dp[i+1][j | bit], dp[i][j] + ai)
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    return dp[m][ALL-1] if dp[m][ALL-1] != INFTY else -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,abcList=readinput()
    ans=solve(n,m,abcList)
    printans(ans)
