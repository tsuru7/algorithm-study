import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
from functools import lru_cache
from itertools import accumulate

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    a=l_input()
    return n,a

@lru_cache(maxsize=None)
def dfs(l, r):
    global cum
    '''
    l と r が休みの場合の生産量
    '''
    if l > 1:
        return dfs(1, r-(l-1))
    if r == l+1:
        return 0
    if r == l+2:
        return a[0]
    if r == l+3:
        return a[0]*2
    ans = 0
    if (r-l-1) % 2 == 0:
        ans = 2*cum[(r-l-1)//2]
    else:
        ans = 2*cum[(r-l-1)//2] + cum[(r-l-1)//2+1]
    # for i in range(l+1, r):
    #     j = min(i-l, r-i)
    #     ans += a[j-1]
    for k in range(l+1, r):
        ans = max(ans, dfs(l, k)+dfs(k, r))
    return ans

cum = None
def solve(n,a):
    global cum
    a.append(a[0])
    cum = list(accumulate(a))
    return dfs(1, n+1)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
