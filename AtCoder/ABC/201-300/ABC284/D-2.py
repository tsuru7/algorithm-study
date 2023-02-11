import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

from bisect import bisect_left, bisect_right
from math import isqrt

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
    t=i_input()
    queries = [i_input() for _ in range(t)]
    return t,queries

def solve(t,queries):
    MAXN = 3*10**6
    # print(MAXN)
    primes = [True for _ in range(MAXN+1)]
    primes[0] = False
    primes[1] = False
    i = 2
    x = i
    while x + i <= MAXN:
        x += i
        primes[x] = False
    for i in range(3, MAXN+1, 2):
        if i*i > MAXN:
            break
        if not primes[i]:
            continue
        x = i
        while x + i <= MAXN:
            x += i
            primes[x] = False
    
    primeList = []
    for i in range(len(primes)):
        if primes[i]:
            primeList.append(i)
    # print(primeList[:10])
    # print(primeList[-10:])
    primeSet = set(primeList)

    prime2List = []
    for p in primeList:
        prime2List.append(p*p)
    prime2Set = set(prime2List)

    ans=[]
    for n in queries:
        for pri in primeList:
            if n % pri == 0:
                # pri は p または q
                x = n // pri
                if x % pri == 0:
                    # もう 1 回 pri で割れたら、p = pri
                    p = pri
                    q = x // pri
                    ans.append((p, q))
                    break
                else:
                    # pri で 1 回しか割れなかったら p = pri
                    q = pri
                    p = isqrt(x)
                    ans.append((p, q))
                    break

    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    t,queries=readinput()
    ans=solve(t,queries)
    printans(ans)
