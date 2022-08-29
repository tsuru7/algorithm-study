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
    x1, y1 = m_input()
    x2, y2 = m_input()
    x3, y3 = m_input()
    return x1, y1, x2, y2, x3, y3

def solve(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1
    ans=(x4, y4)
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    x1, y1, x2, y2, x3, y3=readinput()
    ans=solve(x1, y1, x2, y2, x3, y3)
    printans(ans)
