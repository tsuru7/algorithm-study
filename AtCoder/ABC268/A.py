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
    a=l_input()
    return a

def solve(a):
    counter = Counter(a)
    ans=len(counter)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a=readinput()
    ans=solve(a)
    printans(ans)
