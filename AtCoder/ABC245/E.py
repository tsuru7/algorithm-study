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
    n,m=m_input()
    a=l_input()
    b=l_input()
    c=l_input()
    d=l_input()
    return n,m,a,b,c,d

def solve(n,m,a,b,c,d):
    ablist = [ (x, y) for (x, y) in zip(a, b)]
    cdlist = [ (x, y) for (x, y) in zip(c, d)]
    ablist.sort()
    cdlist.sort()
    j = 0
    for i in range(n):
        if j >= m:
            return 'No'
        a, b = ablist[i]
        c, d = cdlist[j]
        while a > c or b > d:
            j += 1
            if j >= m:
                return 'No'
            c, d = cdlist[j]
        j += 1
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a,b,c,d=readinput()
    ans=solve(n,m,a,b,c,d)
    printans(ans)
