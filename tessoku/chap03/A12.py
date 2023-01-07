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
    return n,k,a

def solve(n,k,a):
    wa = 0
    ac = 10**9
    while ac - wa > 1:
        wj = (wa + ac) // 2
        nprint = 0
        for i in range(n):
            nprint += wj//a[i]
        if nprint >= k:
            ac = wj
        else:
            wa = wj
    return ac

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
