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
    
    def getPrimes(self):
        return self.primes

    def getPrimeList(self):
        primeList = []
        for i, flg in enumerate(self.primes):
            if flg:
                primeList.append(i)
        return primeList


def readinput():
    n=i_input()
    return n

def solve(n):
    primeList = Eratosthenes(10**6).getPrimeList()
    prime3List = [x*x*x for x in primeList]

    ans=0
    for i, pi in enumerate(primeList):
        wa = len(prime3List)
        ac = 0
        while wa - ac > 1:
            wj = (wa + ac) // 2
            if prime3List[wj]*pi > n:
                wa = wj
            else:
                ac = wj
        j = ac
        qj = primeList[j]
        ans += max(0, j-i)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
