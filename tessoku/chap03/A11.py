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
    n,x=m_input()
    a=l_input()
    return n,x,a

def solve(n,x,a):
    # a[wa] < x <= a[ac] となる ac を求める
    if a[0] == x:
        return 1
    wa = 0
    ac = n-1
    while ac - wa > 1:
        wj = (ac+wa)//2
        if a[wj] < x:
            wa = wj
        else:
            ac = wj
    return ac+1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,a=readinput()
    ans=solve(n,x,a)
    printans(ans)
