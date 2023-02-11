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
    r,c=m_input()
    amap = [ l_input() for _ in range(2) ]
    return r,c,amap

def solve(r,c,amap):
    r -= 1
    c -= 1
    ans=amap[r][c]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    r,c,amap=readinput()
    ans=solve(r,c,amap)
    printans(ans)
