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
    for _ in range(n):
        m = i_input()
        factors = []
        for i in range(m):
            p, e = m_input()
            factors.append([p,e])
        factors.sort()
        a.append((m, factors))
    return n,a

def solve(n,a):
    pdict = dict()
    for i, (m, factors) in enumerate(a):
        for j in range(m):
            p, e = factors[j]
            if p in pdict:
                pdict[p].append((e, i))
            else:
                pdict[p] = [(e, i)]
    maxcnt = [0 for _ in range(n)]
    for p, elist in pdict.items():
        elist.sort(reverse=True)
        if len(elist) == 1 or elist[0][0] != elist[1][0]:
            maxcnt[elist[0][1]] += 1
    ans = 0
    for i in range(n):
        if maxcnt[i] > 0:
            ans += 1
    if ans < n:
        ans += 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
