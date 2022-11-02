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
    a=l_input()
    return n,a

def solve(n,a):
    maxa = max(a)
    primes = [True for _ in range(maxa+1)]
    primes[0] = False
    primes[1] = False
    num = 2
    j = num*num
    while j <= maxa:
        primes[j] = False
        j += num
    num = 3
    while num*num <= maxa:
        if primes[num]:
            j = num*num
            primes[j] = False
            j += num
        num += 2
    factcount = dict()
    for d in range(2, maxa+1):
        if not primes[d]:
            continue
        count = 0
        for i in range(n):
            if a[i] % d == 0:
                count += 1
        factcount[d] = count
    setwise = True
    pairwise = True
    for k, v in factcount.items():
        if v > 1:
            pairwise = False
        if v == n:
            setwise = False
    if pairwise:
        return 'pairwise coprime'
    elif setwise:
        return 'setwise coprime'
    else:
        return 'not coprime'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
