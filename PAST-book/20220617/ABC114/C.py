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

def dfs(base, n):
    if base > n:
        return 0
    count = 0
    s = str(base)
    if '3' in s and '5' in s and '7' in s:
        count += 1
    for num in [3, 5, 7]:
        count += dfs(base*10+num, n)
    return count

def solve(n):
    return dfs(0, n)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
