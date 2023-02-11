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
    n,k=m_input()
    a=l_input()
    return n,k,a

def solve(n,k,a):
    a.sort(reverse=True)
    a.append(0)
    i = -1
    ans = 0
    while k > 0:
        i += 1
        if a[i] == 0:
            break
        while a[i+1] == a[i]:
            i += 1
        top = a[i]
        bot = a[i+1] + 1
        dif = a[i] - a[i+1]
        full_count = (i+1) * dif
        if k >= full_count:
            ans += (i+1) * (top + bot) * dif // 2
            k -= full_count
        else:
            count = k // (i+1)
            bot = top - count
            ans += (i+1) * (top + bot) * count // 2
            k -= count * (i+1)
            ans += k * (bot + 1)
            k = 0
    return ans

def printans(ans):
    if isinstance(ans, list) or isinstance(ans, tuple):
        print(*ans, sep='\n')
    else:
        print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
