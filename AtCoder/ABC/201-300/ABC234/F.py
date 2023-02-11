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
    s = input()
    return s

def solve(s):
    MOD = 998244353

    n = len(s)
    counter = Counter(s)
    m = [0]*n
    for i in range(1, n+1):
        count = 0
        for k, v in counter.items():
            if v >= i:
                count += 1
        m[i-1] = count
    print(f'm: {m}')
        
    ans1 = 0
    ans2 = 1
    for i in range(n):
        if m[i] == 0:
            break
        ans2 *= m[i]
        ans2 %= MOD
        ans1 += ans2
        ans1 %= MOD 
    return ans1

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
