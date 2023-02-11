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
    h,w=m_input()
    r,c=m_input()
    return h,w,r,c

def solve(h,w,r,c):
    ans=0
    if h == 1:
        ans += 0
    elif 2 <= r <= h-1:
        ans += 2
    elif r == 1:
        ans += 1
    elif r == h:
        ans += 1
    if w == 1:
        ans += 0
    elif 2 <= c <= w-1:
        ans += 2
    elif c == 1:
        ans += 1
    elif c == w:
        ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,r,c=readinput()
    ans=solve(h,w,r,c)
    printans(ans)
