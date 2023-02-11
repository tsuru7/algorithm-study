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
    x,y=map(int, input().split('.'))
    return x,y

def main(x,y):
    if 0 <= y <= 2:
        return str(x)+'-'
    elif 3 <= y <= 6:
        return str(x)
    else:
        return str(x)+'+'

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y=readinput()
    ans=main(x,y)
    printans(ans)
