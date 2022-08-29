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
    return n,x

def solve(n,x):
    count = 0
    while x > 0:
        count += 1
        x -= n
    

    ans=chr(ord('A')+count-1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x=readinput()
    ans=solve(n,x)
    printans(ans)
