import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations

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
    n,m=m_input()
    slist = [input() for _ in range(n)]
    tlist = [input() for _ in range(m)]
    return n,m,slist,tlist

def dfs(s, n, p, test):
    if len(s) > 16:
        return -1

    if len(p) == 0:
        if 3 <= len(s) <= 16 and s not in test:
            return s
        else:
            return -1

    if n == 0:
        return -1

    for i in range(1, n+1):
        tmp = s + '_'*i + p[0]
        candi = dfs(tmp, n-i, p[1:], test)
        if candi != -1:
            return candi
    return -1

def solve(n,m,slist,tlist):
    tset = set(tlist)
    totlen = 0
    for s in slist:
        totlen += len(s)
    ndelim = 16-totlen
    for p in permutations(slist):
        candi = dfs(p[0], ndelim, p[1:], tset)
        # print(f'candi: {candi}')
        if candi != -1:
            return candi
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,slist,tlist=readinput()
    ans=solve(n,m,slist,tlist)
    printans(ans)
