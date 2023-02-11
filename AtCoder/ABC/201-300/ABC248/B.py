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
    ans=0
    while a < b:
        a *= k
        ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,k=readinput()
    ans=solve(a,b,k)
    printans(ans)
