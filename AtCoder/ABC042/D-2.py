import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
INFTY = sys.maxsize
MOD10 = 10**9+7
MOD99 = 998244353
from functools import lru_cache

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
    h,w,a,b=m_input()
    return h,w,a,b

#memo1 = dict()
@lru_cache(maxsize=None)
def func1(r, c):

    if c == 1:
        return 1
    inv = pow(c-1, MOD10-2, MOD10)
    ans = (r+c-2)*inv*func1(r, c-1)
    ans %= MOD10
    return ans

def func2(r, c, w, b):
    return func1(r, w-b-c+1)

def solve(h,w,a,b):
    ans = 0
    for i in range(1, w-b+1):
        ans += func1(h-a, b+i) * func2(a, i, w, b)
        ans %= MOD10
    # print(memo1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,a,b=readinput()
    ans=solve(h,w,a,b)
    printans(ans)
