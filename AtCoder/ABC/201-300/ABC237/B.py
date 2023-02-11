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
    h,w=m_input()
    amat = [ l_input() for _ in range(h) ]
    return h,w,amat

def solve(h,w,amat):
    bmat = [ [ amat[col][row] for col in range(h) ] for row in range(w) ]
    return bmat

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    h,w,amat=readinput()
    ans=solve(h,w,amat)
    printans(ans)
