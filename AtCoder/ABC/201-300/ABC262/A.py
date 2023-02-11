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
    y=i_input()
    return y

def solve(y):
    r = y % 4
    if r == 0:
        return y + 2
    elif r == 1:
        return y + 1
    elif r == 2:
        return y
    else:
        return y + 3

def printans(ans):
    print(ans)

if __name__=='__main__':
    y=readinput()
    ans=solve(y)
    printans(ans)
