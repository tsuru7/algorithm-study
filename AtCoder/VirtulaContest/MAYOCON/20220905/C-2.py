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
    s = input()
    return n,s

def solve(n,s):
    counter = Counter(s)
    r = counter['R']
    g = counter['G']
    b = counter['B']
    ans=r*g*b
    for i in range(n):
        for j in range(i+1, n):
            k = j + (j-i)
            if k >= n:
                continue
            sijk = s[i]+s[j]+s[k]
            if 'R' in sijk and 'G' in sijk and 'B' in sijk:
                ans -= 1 
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
