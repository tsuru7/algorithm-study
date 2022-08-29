import sys
sys.setrecursionlimit(10**5)
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
    x,y=m_input()
    return x,y

def main(x,y):
    if x == y:
        return x
    else:
        return 3-x-y

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y=readinput()
    ans=main(x,y)
    printans(ans)
