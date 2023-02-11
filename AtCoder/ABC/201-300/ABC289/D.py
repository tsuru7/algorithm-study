import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
from collections import deque, Counter
from itertools import accumulate, permutations
from bisect import bisect_left, bisect_right
from heapq import heapify, heappush, heappop
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353
YES = 'Yes'
NO  = 'No'

input = sys.stdin.readline
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
# DEBUG = False
# def printd(*args):
#     if DEBUG:
#         print(*args)

def readinput():
    n=i_input()
    a=l_input()
    m=i_input()
    b=l_input()
    x = i_input()
    return n,m,a,b,x

def solve(n,m,a,b,x):
    moti = [False]*(10**5+1)
    for bi in b:
        moti[bi] = True
    setb = set(b)
    dp = [set(), set()]
    i = 0
    dp[i].add(0)
    while len(dp[i]) > 0:
        j = 1 - i
        dp[j] = set()
        for step in dp[i]:
            for ai in a:
                y = step + ai
                if y == x:
                    return YES
                elif y < x and not moti[y]:
                    dp[j].add(y)
                elif y > x:
                    break
        i = j
    return NO

def solve2(n,m,a,b,x):
    moti = set(b)
    cand = [set(), set()]
    j = 0
    cand[j].add(0)
    for i in range(n):
        k = 1 - j
        cand[k] = set()
        ai = a[i]
        for x in cand[j]:
            y = x + ai
            while y <= x:
                if y not in moti: cand[k].add(y)
                y += ai
                if y == x:
                    return YES
        j = k
    return NO

def printans(ans):
    if isinstance(ans, list) or isinstance(ans, tuple):
        print(*ans, sep='\n')
    else:
        print(ans)

if __name__=='__main__':
    n,m,a,b,x=readinput()
    ans=solve(n,m,a,b,x)
    printans(ans)
