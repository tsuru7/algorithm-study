import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import Counter

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
    nlist = [i_input() for _ in range(n)]
    return n,m,nlist

def solve(n,m,nlist):
    ncount = Counter(nlist)
    for k, v in ncount.items():
        print(f'key: {k}, value: {v}')
    print(f'nlist: {nlist}')
    cumsum = [[0] for _ in range(m)]
    for nui in nlist:
        for i in range(m):
            if i == nui-1:
                cumsum[i].append(cumsum[i][-1]+1)
            else:
                cumsum[i].append(cumsum[i][-1])

    for i in range(m):
        print(f'i: {i}, cumsum[i]: {cumsum[i]}')

    dp = [[INFTY, 0] for i in range(2**m)]
    dp[0] = [0, 0]
    for state in range(1, 2**m):
        count = 0
        for nui in range(m):
            if state & 1<<nui > 0:
                prev = state ^ 1<<nui
                l = dp[prev][1]
                r = l + ncount[nui+1]-1
                nuicount = cumsum[nui][r+1] - cumsum[nui][l]
                dp[state][0] = min(dp[state][0], dp[prev][0] + ncount[nui] - nuicount)
                count += ncount[nui+1]
        dp[state][1] = count
    
    return dp[-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,nlist=readinput()
    ans=solve(n,m,nlist)
    printans(ans)
