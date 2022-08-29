import sys
from xmlrpc.server import DocXMLRPCRequestHandler
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
    t = input()
    return n,t

def solve(n,t):
    dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    dir = 0
    dx, dy = dxy[dir]
    x = 0
    y = 0
    for c in t:
        if c == 'S':
            x += dx
            y += dy
        else:
            dir += 1
            dir %= 4
            dx, dy = dxy[dir]
    ans=x, y
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,t=readinput()
    ans=solve(n,t)
    printans(ans)
