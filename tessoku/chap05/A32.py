import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
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
    n,a,b=m_input()
    return n,a,b

def solve(n,a,b):
    dp = [False for _ in range(n+1)]
    for i in range(a, n+1):
        if i-a >= 0:
            dp[i] |= not dp[i-a]
        if i-b >= 0:
            dp[i] |= not dp[i-b]
    if dp[i]:
        return 'First'
    else:
        return 'Second'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=solve(n,a,b)
    printans(ans)
