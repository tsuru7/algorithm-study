import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

class Eratosthenes:
    def __init__(self, n):
        self.n = n
        self.primes = [True for _ in range(n+1)]
        self.primes[0] = False
        self.primes[1] = False
        i = 2
        x = i
        while x + i <= n:
            x += i
            self.primes[x] = False
        for i in range(3, n+1, 2):
            if i*i > n:
                break
            if not self.primes[i]:
                continue
            x = i
            while x + i <= n:
                x += i
                self.primes[x] = False
        return
    
    def isPrime(self, x):
        return self.primes[x]

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
    eratosthenes = Eratosthenes(n)
    ans = []
    for i in range(n+1):
        if eratosthenes.isPrime(i):
            ans.append(i)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
