import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
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
    n=i_input()
    return n

memo = None
def f(n):
    global memo
    if memo[n] > 0:
        return memo[n]

    if n == 0:
        return 0

    ans = INFTY
    if n == 1:
        ans = min(ans, 1)
    else:
        ans = min(ans, 1+f(n-1))
    i = 1
    while n-6**i >= 0:
        if n == 6**i:
            ans = min(ans, 1)
        else:
            ans = min(ans, 1+f(n-6**i))
        i += 1
    i = 1
    while n-9**i >= 0:
        if n == 9**i:
            ans = min(ans, 1)
        else:
            ans = min(ans, 1+f(n-9**i))
        i += 1
    memo[n] = ans
    return ans

def solve(n):
    global memo
    memo = [0 for _ in range(n+1)]
    ans=f(n)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
