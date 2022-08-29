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
    a,b,k=m_input()
    return a,b,k

def solve(a,b,k):
    if a >= k:
        return (a-k, b)
    elif a < k <= a+b:
        return (0, a+b-k)
    else:
        return (0, 0)

def printans(ans):
    print(*ans)

if __name__=='__main__':
    a,b,k=readinput()
    ans=solve(a,b,k)
    printans(ans)
