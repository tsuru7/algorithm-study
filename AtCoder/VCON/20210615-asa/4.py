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
    a,b=m_input()
    l=l_input()
    return n,a,b,l

def main(n,a,b,l):
    ans=0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,l=readinput()
    ans=main(n,a,b,l)
    printans(ans)
