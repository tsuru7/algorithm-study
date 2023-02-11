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
    n,a,b=m_input()
    return n,a,b

def main(n,a,b):
    if (a+b) % 2 == 0:
        return (b-a)//2
    return min((b-1+a-1+1)//2, (n-a+n-b+1)//2)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    printans(ans)
