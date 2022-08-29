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
    n,m=m_input()
    a=l_input()
    b=l_input()
    return n,m,a,b

def solve(n,m,a,b):
    counter = Counter(a)
    for i in range(m):
        if b[i] in counter and counter[b[i]] > 0:
            counter[b[i]] -= 1
        else:
            return 'No'
    return 'Yes'
    
def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a,b=readinput()
    ans=solve(n,m,a,b)
    printans(ans)
