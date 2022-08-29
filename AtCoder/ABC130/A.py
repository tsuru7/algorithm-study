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
    x, a=m_input()
    return x,a

def main(x,a):
    if x < a:
        return 0
    else:
        return 10

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,a=readinput()
    ans=main(x,a)
    printans(ans)
