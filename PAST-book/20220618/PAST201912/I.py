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
    items = [ input() for _ in range(m) ]
    return n,m,items

def decode(s):
    i = 0
    for c in s:
        i <<= 1
        if c == 'Y':
            i += 1
    return i

def solve(n,m,items):
    dp = [ [INFTY]*(2**n) for _ in range(m+1) ]
    dp[0][0] = 0
    for i, l in enumerate(items, 1):
        si, ci = l.split()
        ci = int(ci)
        k = decode(si)
        for j in range(2**n):
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            dp[i][j|k] = min(dp[i][j|k], dp[i-1][j]+ci)
    return dp[m][2**n-1] if dp[m][2**n-1] != INFTY else -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,items=readinput()
    ans=solve(n,m,items)
    printans(ans)
