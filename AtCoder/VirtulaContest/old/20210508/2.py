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
    n=i_input()
    k = i_input()
    x = i_input()
    y = i_input()
    return n,k,x,y

def main(n,k,x,y):
    return min(n,k)*x + max(0, n-k)*y

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,x,y=readinput()
    ans=main(n,k,x,y)
    printans(ans)
