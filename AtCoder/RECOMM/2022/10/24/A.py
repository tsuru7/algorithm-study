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
    fmap = [l_input() for _ in range(n)]
    pmap = [l_input() for _ in range(n)]
    return n,fmap,pmap

def solve(n,fmap,pmap):
    ALL = 1<<10
    ans=-INFTY
    for opens in range(1, ALL):
        rieki = 0
        for shop in range(n):
            count = 0
            for period in range(10):
                bit = 1<<period
                if opens & bit > 0 and fmap[shop][period] == 1:
                    count += 1
            rieki += pmap[shop][count]
        ans = max(ans, rieki)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,fmap,pmap=readinput()
    ans=solve(n,fmap,pmap)
    printans(ans)
