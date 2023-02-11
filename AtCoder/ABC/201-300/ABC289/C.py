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
    n,m=m_input()
    sList = []
    for _ in range(m):
        _ = i_input()
        sList.append(l_input())
    return n,m,sList

def solve(n,m,sList):
    ALL = 2**m
    ans=0
    for x in range(1, ALL):
        count = [False]*n
        for i in range(n):
            b = 1<<i
            if x & b > 0:
                s = sList[i]
                for c in s:
                    count[c-1] = True
        if sum(count) == n:
            ans += 1
    return ans

def solve2(n,m,sList):
    ALL = 2**m
    ans=0
    for x in range(1, ALL):
        tmpset = set()
        for i in range(m):
            b = 1<<i
            if x & b > 0:
                tmpset = tmpset.union(set(sList[i]))
        if len(tmpset) == n:
            ans += 1
    return ans

def printans(ans):
    if isinstance(ans, list) or isinstance(ans, tuple):
        print(*ans, sep='\n')
    else:
        print(ans)

if __name__=='__main__':
    n,m,sList=readinput()
    ans=solve2(n,m,sList)
    printans(ans)
