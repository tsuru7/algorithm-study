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
    setb = set(b)
    dp = [False]*(x+1)
    dp[0] = True
    for i in range(x):
        for aj in a:
            if i+aj <= x:
                if i+aj not in setb:
                    dp[i+aj] |= dp[i]
    if dp[x]:
        return YES
    else:
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
