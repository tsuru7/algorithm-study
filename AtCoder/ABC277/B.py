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
    # print(sList)
    counter = Counter(sList)
    # print(counter)
    for k, v in counter.items():
        # print(k, v)
        if v > 1:
            return 'No'
    for i in range(n):
        si = sList[i]
        c1 = si[0]
        c2 = si[1]
        if c1 not in ['H', 'D', 'C', 'S']:
            return 'No'
        if c2 not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,sList=readinput()
    ans=solve(n,sList)
    printans(ans)
