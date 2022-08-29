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
    return h,w

def solve(h,w):
    if h == 1 or w == 1:
        return h*w
    if h % 2 == 0:
        tate = h // 2
    else:
        tate = h // 2 + 1
    if w % 2 == 0:
        yoko = w // 2
    else:
        yoko = w // 2 + 1
    ans=tate*yoko
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w=readinput()
    ans=solve(h,w)
    printans(ans)
