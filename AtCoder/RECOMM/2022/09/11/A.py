# https://atcoder.jp/contests/abc124/tasks/abc124_d

import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate

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
    n,k=m_input()
    s = input()
    return n,k,s

def solve(n,k,s):
    '''
    101    のときは1回
    010    のときは2回で全て1にできる

    1010   のときは2回
    0101   のときは2回で全て1にできる

    10101  のときは2回               切り替え回数//2
    01010  のときは3回

    101010 のときは3回               切り替え回数//2
    010101 のときは3回

    1回の反転で3つのパートが同じ向きになる
    2回の反転で5つのパートが同じ向きになる
    ...
    k回の反転で2*k+1個のパートが同じ向きになる
    逆立ちした人の最大数を求めるので、1で挟まれた領域を最大にする
    '''
    comp = []
    onestart = (s[0] == '1')
    oneend = (s[-1] == '1')
    pre = s[0]
    comp.append(1)
    for i in range(1, n):
        if s[i] == pre:
            comp[-1] += 1
        else:
            comp.append(1)
        pre = s[i]
    if len(comp) % 2 == 1:
        if onestart:
            l = len(comp)//2
        else:
            l = len(comp)//2 + 1
    else:
        l = len(comp)//2
    if l <= k:
        return n
    
    print(f'comp: {comp}')

    cum = [0] + list(accumulate(comp))

    print(f'cum: {cum}')

    if (onestart and k % 2 == 0) or (not onestart and k % 2 == 1):
        l = 0
    else:
        l = 1
    r = l + 2*k+1
    ans=0
    while r < len(comp):
        ans = max(ans, cum[r]-cum[l])
        l += 2
        r += 2

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,s=readinput()
    ans=solve(n,k,s)
    printans(ans)
