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
    r = l_input()
    c = l_input()
    amat = [l_input() for _ in range(h)]
    return h,w,r,c,amat

def solve(h,w,r,c,amat):
    dp = [[0 for _ in range(w)] for _ in range(h)]
    for 
    ans=0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,r,c,amat=readinput()
    ans=solve(h,w,r,c,amat)
    printans(ans)
