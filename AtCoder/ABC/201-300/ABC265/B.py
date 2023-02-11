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
    n,m,t=m_input()
    a=l_input()
    xyList = [l_input() for _ in range(m)]
    return n,m,t,a,xyList

def solve(n,m,t,a,xyList):
    bonus = [0 for _ in range(n)]
    for x, y in xyList:
        bonus[x-1] = y
    time = t
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            return 'No'
        time += bonus[i+1]
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,t,a,xyList=readinput()
    ans=solve(n,m,t,a,xyList)
    printans(ans)
