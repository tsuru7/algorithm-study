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
    a,b,c,d=m_input()
    return a,b,c,d

def solve(a,b,c,d):
    MAX = b+d
    MIN = a+c
    primes = [True]*(MAX+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, MAX+1):
        x = i
        if not primes[x]:
            continue
        x += i
        while x <= MAX:
            primes[x] = False
            x += i
    primeonly = [MIN-1] # 番兵
    for i in range(MIN, MAX+1):
        if primes[i]:
            primeonly.append(i)
    primeonly.append(MAX+1) # 番兵
    maxdif = 0
    for i in range(1, len(primeonly)):
        maxdif = max(maxdif, primeonly[i]-primeonly[i-1])
    if maxdif > d-c+1:
        return 'Takahashi'
    else:
        return 'Aoki'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,d=readinput()
    ans=solve(a,b,c,d)
    printans(ans)
