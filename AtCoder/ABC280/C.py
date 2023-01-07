import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    t = input()
    return s, t

def solve(s, t):
    n = len(s)
    for i in range(n):
        if t[i] != s[i]:
            return i+1
    return n+1

def printans(ans):
    print(ans)

if __name__=='__main__':
    s, t=readinput()
    ans=solve(s, t)
    printans(ans)
