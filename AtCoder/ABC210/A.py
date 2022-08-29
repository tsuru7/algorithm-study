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
    n,a,x,y=m_input()
    return n,a,x,y

def main(n,a,x,y):
    if n <= a:
        ans = n*x
    else:
        ans= a*x + (n-a)*y
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,x,y=readinput()
    ans=main(n,a,x,y)
    printans(ans)
