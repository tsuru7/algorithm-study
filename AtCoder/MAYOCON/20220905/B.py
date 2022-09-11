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
    w = input()
    return w

def solve(w):
    counter = Counter(w)
    for _, v in counter.items():
        if v % 2 == 0:
            continue
        else:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    w=readinput()
    ans=solve(w)
    printans(ans)
