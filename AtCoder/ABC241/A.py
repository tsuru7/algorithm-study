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
    a=l_input()
    return a

def solve(a):
    ans = 0
    for i in range(3):
        ans=a[ans]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a=readinput()
    ans=solve(a)
    printans(ans)
