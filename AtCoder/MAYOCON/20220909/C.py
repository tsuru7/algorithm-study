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
    a,b,x=m_input()
    return a,b,x

def solve(a,b,x):
    ac = 0
    wa = x
    while wa - ac > 1:
        wj = (wa+ac)//2
        if a*wj + b*len(str(wj)) <= x:
            ac = wj
        else:
            wa = wj
    return min(10**9, ac)

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,x=readinput()
    ans=solve(a,b,x)
    printans(ans)
