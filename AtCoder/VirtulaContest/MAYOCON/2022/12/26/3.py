import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353
from bisect import bisect_left, bisect_right

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

def solve(n):
    primes = [True for _ in range(10**6+1)]
    primes[0] = False
    primes[1] = False
    p = 2
    x = p*2
    while x <= 10**6:
        primes[x] = False
        x += p
    for p in range(3, 10**6+1, 2):
        x = p*2
        while x <= 10**6:
            primes[x] = False
            x += p
    primeList = []
    for i in range(10**6+1):
        if primes[i]:
            primeList.append(i)
    m = len(primeList)
    print(m)
    ans=0
    for i in range(1, m):
        p = primeList[i]
        p3 = p**3
        x = n//p3
        idx = bisect_left(primeList, x)
        if i <= 10:
            print(f'i: {i}, p: {p}, x: {x}, idx: {idx}')
        if idx == 0 and x < p[0]:
            continue
        if idx >= i:
            continue
        ans += idx+1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
