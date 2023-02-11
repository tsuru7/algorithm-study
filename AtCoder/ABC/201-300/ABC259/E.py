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
    a = []
    primes = set()
    for _ in range(n):
        m = i_input()
        factors = []
        for i in range(m):
            p, e = m_input()
            primes.add(p)
            factors.append([p,e])
        factors.sort()
        a.append((m, factors))
    primes = sorted(list(primes))
    nprimes = len(primes)
    pidx = dict()
    for i in range(nprimes):
        pi = primes[i]
        pidx[pi] = i
    pmap = [[(0,0) for i in range(n)] for j in range(nprimes)]
    for i in range(n):
        mi, factors = a[i]
        for p, e in factors:
            pmap[pidx[p]][i] = (e, i)
    return n,a,pmap

def solve(n,a,pmap):
    if n == 1:
        return 1
    maxlist = [[] for _ in range(n)]
    for plist in pmap:
        plist.sort(reverse=True)
        if plist[0][0] != plist[1][0]:
            maxlist[plist[0][1]].append(plist[0][0])
    ans = 0
    zerocnt = 0
    for i in range(n):
        if len(maxlist[i]) > 0:
            ans += 1
        else:
            zerocnt += 1
    if zerocnt > 0:
        ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,pmap=readinput()
    ans=solve(n,a,pmap)
    printans(ans)
