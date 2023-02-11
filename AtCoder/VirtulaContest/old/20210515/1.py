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
    t,x=m_input()
    return t,x

def main(t,x):
    ans=t/x
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    t,x=readinput()
    ans=main(t,x)
    printans(ans)
