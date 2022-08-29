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
    s = input()
    return n,s

def solve(n,s):
    ans=0
    for c1 in '0123456789':
        p1 = s.find(c1)
        if p1 < 0:
            continue
        for c2 in '0123456789':
            p2 = s.find(c2, p1+1)
            if p2 < 0:
                continue
            for c3 in '0123456789':
                p3 = s.find(c3, p2+1)
                if p3 < 0:
                    continue
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
