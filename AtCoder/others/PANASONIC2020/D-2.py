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
    return n

def dfs(now, n):
    # print(f'now: {now}, n: {n}')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(now) == n:
        return [now]
    counter = Counter(now)
    # print(f'counter: {counter}')
    if len(counter) == 0:
        ans = dfs('a', n)
    else:
        ans = []
        for k in counter.keys():
            ans += dfs(now + k, n)
        ans += dfs(now + alphabet[len(counter)], n)
    return ans

def solve(n):
    ans=dfs('', n)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
