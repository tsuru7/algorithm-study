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
    sList = [input() for _ in range(n)]
    tList = [input() for _ in range(m)]
    return n,m,sList,tList

def dfs(now, maxdelim, p, tset):
    if len(now) > 16:
        return -1

    if len(p) == 0:
        if now not in tset and 3 <= len(now) <= 16:
            return now
        else:
            return -1
    
    if maxdelim <= 0:
        return -1
    
    for ndelim in range(1, maxdelim+1):
        ans = dfs(now+'_'*ndelim+p[0], maxdelim-ndelim, p[1:], tset)
        if ans != -1:
            return ans
    return -1


def solve(n,m,sList,tList):
    tset = set(tList)
    if n == 1:
        cand = sList[0]
        if cand not in tset and 3 <= len(cand) <= 16:
            return cand
        else:
            return -1

    slen = [len(sList[i]) for i in range(n)]
    stotal = sum(slen)

    for p in permutations(sList):
        cand = dfs(p[0], 16-stotal, p[1:], tset)
        if cand != -1:
            return cand
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,sList,tList=readinput()
    ans=solve(n,m,sList,tList)
    printans(ans)
