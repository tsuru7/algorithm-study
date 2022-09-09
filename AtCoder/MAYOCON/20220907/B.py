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
    sList = [input() for _ in range(n)]
    return n,sList

def solve(n,sList):
    counter = Counter(sList)
    ans = []
    _, m = counter.most_common(1)[0]
    for k, v in counter.most_common():
        if v == m:
            ans.append(k)
    return sorted(ans)

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,sList=readinput()
    ans=solve(n,sList)
    printans(ans)
