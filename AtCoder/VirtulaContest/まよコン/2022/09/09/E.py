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
    divisors = set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
        i += 1
    divisors.discard(1)
    candidates = set()
    for d in divisors:
        x = n
        while x % d == 0:
            x //= d
        # print(f'x: {x}, d: {d}, x % d: {x%d}')
        if x % d == 1:
            candidates.add(d)
    divisors = set()
    i = 1
    while i*i <= n-1:
        if (n-1) % i == 0:
            divisors.add(i)
            divisors.add((n-1)//i)
        i += 1
    divisors.discard(1)
    ans = divisors.union(candidates)
    return len(ans)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
