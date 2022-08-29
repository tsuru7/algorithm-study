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
    nui0 = [i_input()-1 for _ in range(n)]
    return n,m,nui0

def solve(n,m,nui0):

    # print(f'nui0: {nui0}')

    nuicnt = Counter(nui0)

    # print(f'nuicnt: {nuicnt}')

    cum = [[0 for i in range(n)] for j in range(m)]
    cum[nui0[0]][0] = 1
    for i in range(1, n):
        nui = nui0[i]
        for j in range(m):
            if j == nui:
                cum[j][i] = cum[j][i-1]+1
            else:
                cum[j][i] = cum[j][i-1]

    # print(*cum, sep='\n')

    ALL = 2**m
    dp = [INFTY for _ in range(ALL)]
    nuilen = [0 for _ in range(ALL)]
    dp[0] = 0
    for state in range(1, ALL):
        for nui in range(m):
            bit = 1<<nui
            if state & bit > 0:
                statek = state^bit
                lk = nuilen[statek]
                rk = lk + nuicnt[nui]-1

                # print(f'state: {bin(state)[2:]}, statek: {bin(statek)[2:]}, lk: {lk}, rk: {rk}')

                if lk > 0:
                    numnui = cum[nui][rk] - cum[nui][lk-1]
                else:
                    numnui = cum[nui][rk]
                nuichg = nuicnt[nui] - numnui
                dp[state] = min(dp[state], dp[statek]+nuichg)
                
                nuilen[state] = rk+1

    # print(f'nuilen: {nuilen}')
    # print(f'dp: {dp}')

    return dp[-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,nui0=readinput()
    ans=solve(n,m,nui0)
    printans(ans)
