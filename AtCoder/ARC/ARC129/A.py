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
    n,l,r=m_input()
    return n,l,r

def f(n,r,k):

    rmin = 

def solve(n,l,r):
    ns = bin(n)[2:]
    rs = bin(r)[2:]
    lens = len(ns)
    lenr = len(rs)
    lenx = max(lens, lenr)
    ns = ('0'*lenx+ns)[-lenx:]
    rs = ('0'*lenx+rs)[-lenx:]
    if ns[0] == rs[0]:
    ans=0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l,r=readinput()
    ans=solve(n,l,r)
    printans(ans)
