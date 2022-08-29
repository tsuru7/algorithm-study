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
    v,a,b,c=m_input()
    return v,a,b,c

def solve(v,a,b,c):
    while True:
        if v < a:
            return 'F'
        v -= a
        if v < b:
            return 'M'
        v -= b
        if v < c:
            return 'T'
        v -= c

def printans(ans):
    print(ans)

if __name__=='__main__':
    v,a,b,c=readinput()
    ans=solve(v,a,b,c)
    printans(ans)
