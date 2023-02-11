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
    x,y,a,b,c=m_input()
    return x,y,a,b,c

def judge(x,y,a,b,c):
    if a % x == 0:
        y -= a // x
    else:
        y -= (a // x + 1)
    if y <= 0:
        return False

    y0 = y
    if b % x == 0:
        y -= b // x
    else:
        y -= (b // x + 1)
    if y <= 0:
        return False

    if c <= x*y:
        return True

    y = y0
    if b % y == 0:
        x -= b // y
    else:
        x -= (b // y + 1)
    if x <= 0:
        return False

    if c <= x*y:
        return True
    
    return False

def main(x,y,a,b,c):
    if judge(x,y,a,b,c) or judge(x,y,a,c,b) or judge(x,y,b,a,c) or judge(x,y,b,c,a) or judge(x,y,c,a,b) or judge(x,y,c,b,a):
        return 'Yes'
    elif judge(y,x,a,b,c) or judge(y,x,a,c,b) or judge(y,x,b,a,c) or judge(y,x,b,c,a) or judge(y,x,c,a,b) or judge(y,x,c,b,a):
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y,a,b,c=readinput()
    ans=main(x,y,a,b,c)
    printans(ans)
