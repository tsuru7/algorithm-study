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
    lrlist = [ l_input() for _ in range(n) ]
    return n,lrlist

def solve(n,lrlist):
    lrlist.sort()
    ans=[]
    ltmp, rtmp = lrlist
    for l, r in lrlist:
        
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,lrlist=readinput()
    ans=solve(n,lrlist)
    printans(ans)
