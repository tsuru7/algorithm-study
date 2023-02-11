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
    b=l_input()
    c=l_input()
    return n,a,b,c

def solve(n,a,b,c):
    a.sort()
    b.sort()
    c.sort()
    ans=0
    # print(f'a: {a}')
    # print(f'b: {b}')
    # print(f'c: {c}')
    for bi in b:
        ai = bisect_left(a, bi)
        ci = bisect_right(c, bi)
        ci = n - ci
        # print(f'ai: {ai}, ci: {ci}')
        ans += ai * ci 
    return ans

def printans(ans):
    if isinstance(ans, list) or isinstance(ans, tuple):
        print(*ans, sep='\n')
    else:
        print(ans)

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=solve(n,a,b,c)
    printans(ans)
