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
    n,x=m_input()
    ablist = [l_input() for _ in range(n)]
    return n,x,ablist

def solve(n,x,ablist):
    ans = INFTY
    base = 0
    for i in range(min(x, n)):
        ai, bi = ablist[i]
        tmp = base + ai+bi*(x-i)
        ans = min(ans, tmp)
        base += ai+bi
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,ablist=readinput()
    ans=solve(n,x,ablist)
    printans(ans)
