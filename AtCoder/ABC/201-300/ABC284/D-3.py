import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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

def isqrt(x):
    ac = 0
    wa = 3*10**9+1
    while wa - ac > 1:
        wj = (wa + ac) // 2
        if wj * wj > x:
            wa = wj
        else:
            ac = wj
    return ac

def solve(t,queries):
    MAXN = 3*10**6
    primeList = Eratosthenes(MAXN).getPrimeList()

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
