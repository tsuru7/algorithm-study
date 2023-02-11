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
    n,m,d=m_input()
    return n,m,d

def solve(n,m,d):
    if d == 0:
        ans = (m-1)/n
    else:
        ans = 2*(m-1)*(n-d)/n**2
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,d=readinput()
    ans=solve(n,m,d)
    printans(ans)
