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

# input = sys.stdin.readline
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
    a=l_input()
    return n,m,a

def solve(n,m,a):
    a = [x-1 for x in a]
    seta = set(a)
    # print(f'seta: {seta}')
    seq = []
    tmp = [0]
    for i in range(n):
        # print(f'i: {i}')
        if i in seta:
            tmp.append(i+1)
        else:
            tmp.reverse()
            seq.append(tmp)
            if i+1 < n:
                tmp = [i+1]
    return seq

def printans(ans):
    for a in ans:
        a = [x+1 for x in a]
        print(*a, end=' ')
    print()

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
