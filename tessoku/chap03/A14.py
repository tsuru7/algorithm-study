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
    n,k=m_input()
    a=l_input()
    b=l_input()
    c=l_input()
    d=l_input()
    return n,k,a,b,c,d

def solve(n,k,a,b,c,d):
    abset = set()
    cdset = set()
    for i in range(n):
        ai = a[i]
        ci = c[i]
        for j in range(n):
            bj = b[j]
            dj = d[j]
            abset.add(ai+bj)
            cdset.add(ci+dj)
    for ab in abset:
        if k - ab in cdset:
            return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a,b,c,d=readinput()
    ans=solve(n,k,a,b,c,d)
    printans(ans)
