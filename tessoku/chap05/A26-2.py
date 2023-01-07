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
    q=i_input()
    queries = [i_input() for _ in range(q)]
    return q,queries

def solve(q,queries):
    MAXX = 300000
    primes = [True for _ in range(MAXX+1)]
    primes[0] = False
    primes[1] = False
    i = 2
    x = i
    while x + i <= MAXX:
        x += i
        primes[x] = False
    for i in range(3, MAXX+1, 2):
        if not primes[i]:
            continue
        x = i
        while x + i <= MAXX:
            x += i
            primes[x] = False
    
    ans=[]
    for x in queries:
        if primes[x]:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    q,queries=readinput()
    ans=solve(q,queries)
    printans(ans)
