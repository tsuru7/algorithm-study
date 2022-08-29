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
    l1,r1,l2,r2=m_input()
    return l1,r1,l2,r2

def solve(l1,r1,l2,r2):
    ans=max(0, min(r1,r2)-max(l1,l2))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    l1,r1,l2,r2=readinput()
    ans=solve(l1,r1,l2,r2)
    printans(ans)
