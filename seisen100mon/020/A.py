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
    a=l_input()
    b=l_input()
    c=l_input()
    return n,a,b,c

def solve(n,a,b,c):
    ans=0
    a.sort()
    b.sort()
    c.sort()
    for bi in b:
        ac = -1
        wa = n
        while wa - ac > 1:
            wj = (ac+wa)//2
            if a[wj] < bi:
                ac = wj
            else:
                wa = wj
        na = ac+1
        ac = -1
        wa = n
        while wa - ac > 1:
            wj = (ac+wa)//2
            if c[wj] <= bi:
                ac = wj
            else:
                wa = wj
        nc = n-1 - ac
        ans += na*nc
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=solve(n,a,b,c)
    printans(ans)
