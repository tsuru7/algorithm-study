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

def getDivisors(n):
    ans = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            ans.append((i, n//i))
            if i*i < n:
                ans.append((n//i, i))
        i += 1
    return ans

def solve(n,a):
    counter = Counter(a)
    divisors = dict()
    for i in range(n):
        ai = a[i]
        if ai in divisors:
            continue
        divisors[ai] = getDivisors(ai)
    
    ans=0
    for i in range(n):
        ai = a[i]
        # print(f'ai: {ai}, divisors: {divisors[ai]}')
        for x, y in divisors[ai]:
            if x not in counter or y not in counter:
                continue
            ans += counter[x] * counter[y]
    return ans

def solve2(n,a):
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
    printans(ans)
    # ans = solve2(n,a)
    # printans(ans)