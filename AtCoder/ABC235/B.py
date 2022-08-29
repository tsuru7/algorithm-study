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
    n=i_input()
    h=l_input()
    return n,h

def solve(n,h):
    i = 0
    while i < n-1 and h[i+1] > h[i]:
        i += 1
    ans=h[i]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,h=readinput()
    ans=solve(n,h)
    printans(ans)
