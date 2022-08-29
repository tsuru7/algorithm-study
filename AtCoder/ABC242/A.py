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
    a,b,c,x=m_input()
    return a,b,c,x

def solve(a,b,c,x):
    if x <= a:
        ans = 1.0
    elif a < x <=b:
        ans = c/(b-a)
    else:
        ans = 0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,x=readinput()
    ans=solve(a,b,c,x)
    printans(ans)
