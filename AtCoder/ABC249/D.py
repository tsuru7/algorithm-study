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
    n=i_input()
    a=l_input()
    return n,a

def solve(n,a):
    counter = Counter(a)
    amax = max(a)
    ans=0
    for q in range(1, amax+1):
        rmax = amax // q
        for r in range(1, rmax+1):
            ans += counter[q]*counter[r]*counter[q*r]


    return ans

def debug(n, a):
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i] == a[j]*a[k]:
                    ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    # ans2 = debug(n, a)
    # if ans != ans2:
    #     print(f'a: {a}')
    printans(ans)
