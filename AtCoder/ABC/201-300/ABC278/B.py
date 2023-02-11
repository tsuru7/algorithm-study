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
    h,m=m_input()
    return h,m

def check(h,m):
    hh = h // 10
    hl = h % 10
    mh = m // 10
    ml = m % 10
    if hh == 0 and hl <= 5:
        return True
    if hh == 1 and hl <= 5:
        return True
    if hh == 2 and mh <= 3 and hl <= 5:
        return True
    return False

def solve(h,m):
    hm = h*60+m
    for i in range(24*60):
        x = hm + i
        h_ = x // 60
        h_ %= 24
        m_ = x % 60
        if check(h_, m_):
            return (h_, m_)

def printans(ans):
    print(*ans)

if __name__=='__main__':
    h,m=readinput()
    ans=solve(h,m)
    printans(ans)
