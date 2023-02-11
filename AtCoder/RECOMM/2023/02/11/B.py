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
    counter = Counter(a)
    attr = list(counter.keys())
    attr.sort(reverse=True)
    attr.append(0)
    # print(f'attr: {attr}')

    iattr = 0
    nattr = 0
    ans = 0
    while k > 0 and iattr < len(counter):
        nattr += counter[attr[iattr]]
        top = attr[iattr]
        bot = attr[iattr+1] + 1
        dif = top - bot + 1
        kaisu = min(k // nattr, dif)
        bot = top - kaisu + 1
        # print(f'nattr: {nattr}, top: {top}, bot: {bot}, dif: {dif}, kaisu: {kaisu}')
        ans += (top + bot) * nattr * kaisu // 2
        # print(f'ans: {ans}')
        k -= kaisu * nattr
        # print(f'k: {k}')
        if k <= nattr:
            ans += (top - kaisu) * k
            k = 0
        iattr += 1
    
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
