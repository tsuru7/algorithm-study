import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict

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

class Osa_k:
    '''
    osa_k法で高速に素因数分解する(O(log(nmax)))
    https://osak.jp/diary/diary_201310.html#20131017
    '''
    def __init__(self, nmax):
        '''
        nmax: 素因数分解する可能性のある数の最大値
        '''
        self.min_factor = [i for i in range(nmax+1)]
        self.primes = [True for _ in range(nmax+1)]
        self.primes[0] = False
        self.primes[1] = False
        num = 2
        j = num*2
        while j <= nmax:
            self.primes[j] = False
            self.min_factor[j] = num
            j += num
        num = 3
        while num*num <= nmax:
            if self.primes[num]:
                j = num*num
                while j <= nmax:
                    self.primes[j] = False
                    self.min_factor[j] = num
                    j += num
            num += 2
        return
    
    def factorization(self, n):
        '''nを素因数分解する
        戻り値: factList = [[prime1, exp1], [prime2, exp2],...] 
                n=(prime1)**exp1 * (prime2)**exp2 * ...
        '''

        factDict=dict()
        while n > 1:
            fact = self.min_factor[n]
            if fact not in factDict:
                factDict[fact] = 1
            else:
                factDict[fact] += 1
            n //= fact

        factList = []
        for fact, order in factDict.items():
            factList.append((fact, order))
        return factList

#
# ABC177-E
#
def readinput():
    n=i_input()
    a=l_input()
    return n,a

def solve(n,a):
    '''
    各Aiを素因数分解する。各素因数の指数は考えなくて良い
    setwiseは全てのAiに対して共通する素因数がないことを意味する。
    pairwiseはどのAi, Ajも共通する素因数を持たないことを意味する。
    それぞれの素因数が何個のAiに含まれるかを dict で管理する
    すべての素因数の個数がn個未満であればsetwise
    さらにすべての素因数の個数が1個以下であればpairwise
    '''
    maxa = max(a)
    osa_k = Osa_k(maxa)
    primes_count = defaultdict(int)
    pairwise = True
    setwise = True
    for i in range(n):
        factList = osa_k.factorization(a[i])
        for prime, order in factList:
            if prime == 1:
                continue
            primes_count[prime] += 1
    for k, v in primes_count.items():
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
