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
    l,r=m_input()
    return l,r

def solve(l,r):
    s = 'atcoder'
    return s[l-1:r]

def printans(ans):
    print(ans)

if __name__=='__main__':
    l,r=readinput()
    ans=solve(l,r)
    printans(ans)
