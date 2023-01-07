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
    n,k=m_input()
    return n,k

def solve(n,k):
    MOD = 10**9+7
    ans=0
    for i in range(k, n+1):
        m = n-i
        min_ = i*(i-1)//2
        max_ = n*(n+1)//2 - m*(m-1)//2
        ans += max_ - min_ + 1
        ans %= MOD
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
