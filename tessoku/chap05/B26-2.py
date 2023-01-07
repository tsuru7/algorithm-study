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
    n=i_input()
    return n

def solve(n):
    primes = [True for _ in range(n+1)]
    primes[0] = False
    primes[1] = False
    i = 2
    x = i
    while x + i <= n:
        x += i
        primes[x] = False
    for i in range(3, n+1, 2):
        if i*i > n:
            break
        if not primes[i]:
            continue
        x = i
        while x + i <= n:
            x += i
            primes[x] = False
    ans = []
    for i in range(n+1):
        if primes[i]:
            ans.append(i)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
