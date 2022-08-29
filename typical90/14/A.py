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
    return n,a,b

def solve(n,a,b):
    a.sort()
    b.sort()
    ans=0
    for i in range(n):
        ans += abs(a[i]-b[i])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=solve(n,a,b)
    printans(ans)
