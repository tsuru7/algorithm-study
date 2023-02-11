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
    a,b,c,d=m_input()
    return a,b,c,d

def solve(a,b,c,d):
    takahashi = (a*60+b)*60
    aoki = (c*60+d)*60+1
    if takahashi < aoki:
        return 'Takahashi'
    else:
        return 'Aoki'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,d=readinput()
    ans=solve(a,b,c,d)
    printans(ans)
