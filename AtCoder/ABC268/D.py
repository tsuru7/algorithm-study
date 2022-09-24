import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations
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

def readinput():
    n,m=m_input()
    sList = [input() for _ in range(n)]
    tList = [input() for _ in range(m)]
    return n,m,sList,tList

def solve(n,m,sList,tList):
    tset = set(tList)
    if n == 1:
        s1 = sList[0]
        cand = s1
        if cand not in tset and 3 <= len(cand) <= 16:
            return cand
        else:
            return -1

    # n > 1
    slen = [len(sList[i]) for i in range(n)]
    stotal = sum(slen)
    max_delim = 16 - stotal
    min_delim = n-1
    delim = defaultdict(list)
    delim[min_delim] = [['_' for _ in range(n-1)]]

    # print(f'delim[min_delim]: {delim[min_delim]}')
    # print(f'max_delim: {max_delim}')

    for l in range(min_delim+1, max_delim+1):
        for d in delim[l-1]:
            for k in range(n-1):
                dd = d.copy()
                dd[k] += '_'
                delim[l].append(dd)
    delim_all = []
    for k, v in delim.items():
        delim_all += v

    # print(f'delim_all: {delim_all}')

    for p in permutations(range(n)):
        for delim in delim_all:
            cand = sList[p[0]]
            for i in range(1, n):
                cand += delim[i-1] + sList[p[i]]
            if cand not in tset:
                return cand
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,sList,tList=readinput()
    ans=solve(n,m,sList,tList)
    printans(ans)
