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
    h,w=m_input()
    return h,w

def solve(h,w):
    n = h-1 + w-1
    r = min(h-1, w-1)
    MOD = 10**9 + 7
    ans = 1
    for i in range(r):
        bunsi = n-i
        bunbo = pow(r-i, MOD-2, MOD)
        ans *= bunsi
        ans %= MOD
        ans *= bunbo
        ans %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w=readinput()
    ans=solve(h,w)
    printans(ans)
