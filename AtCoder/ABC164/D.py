import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict

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
    count = defaultdict(int)
    s = s[::-1]
    n = len(s)
    # print(f'n: {n}')
    MOD = 2019
    t = [0 for _ in range(n+1)]
    t[0] = int(s[0]) % MOD
    # print(f'i: 0, t[i]: {t[0]}')
    count[t[0]] += 1
    for i in range(1, n):
        t[i] = int(s[i])*pow(10, i, MOD) + t[i-1]
        t[i] %= MOD
        # print(f'i: {i}, t[i]: {t[i]}')
        count[t[i]] += 1
    t[n] = 0
    count[t[n]] += 1
    # print(f'count: {count}')
    ans=0
    for k, v in count.items():
        ans += v*(v-1)//2

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
