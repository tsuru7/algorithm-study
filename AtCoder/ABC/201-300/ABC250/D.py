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

def get_primes():
    n = 10**6
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, n+1):
        if not primes[i]:
            continue
        j = i+i
        while j <= n:
            primes[j] = False
            j += i
    ans = []
    for i in range(2, n+1):
        if primes[i]:
            ans.append(i)
    return ans

def readinput():
    n=i_input()
    return n

def numq(i, n, primes):
    if i == len(primes)-1:
        return 0
    p = primes[i]
    q = primes[i+1]
    if p*q*q*q > n:
        return 0
    l = i+1
    r = len(primes)-1
    while r - l > 1:
        m = (l+r)//2
        q = primes[m]
        if p*q*q*q <= n:
            l = m
        else:
            r = m
    return l-i


def solve(n):
    primes = get_primes()
    # print(f'primes: {primes}')
    # print(f'len(primes): {len(primes)}')
    ans=0
    nprimes = len(primes)
    for i in range(nprimes):
        p = primes[i]
        ans += numq(i, n, primes)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
