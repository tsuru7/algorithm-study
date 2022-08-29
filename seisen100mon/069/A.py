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
    queries = [l_input() for _ in range(q)]
    return q, queries

def solve(q, queries):
    primes = [True if i % 2 == 1 else False for i in range(10**5+1)]
    primes[0] = False
    primes[1] = False
    primes[2] = True
    i = 3
    while i <= 10**5:
        if primes[i]:                
            n = 2
            while i*n <= 10**5:
                primes[i*n] = False
                n += 1
        i += 2
    cprim = [0 for i in range(10**5+1)]
    for i in range(3, 10**5+1):
        if i % 2 == 1 and primes[i] and primes[(i+1)//2]:
            cprim[i] = cprim[i-1] + 1
        else:
            cprim[i] = cprim[i-1]
    # print(f'primes: {primes[:10]}')
    # print(f'cprim: {cprim[:10]}')
    ans=[]
    for l, r in queries:
        ans.append(cprim[r]-cprim[l-1])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    q, queries=readinput()
    ans=solve(q, queries)
    printans(ans)
