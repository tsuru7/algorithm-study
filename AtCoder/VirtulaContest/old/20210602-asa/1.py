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
    k=i_input()
    x=l_input()
    return n,k,x

def main(n,k,x):
    ans=0
    for i in range(n):
        ans += min(x[i], k-x[i])
    return ans*2

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,x=readinput()
    ans=main(n,k,x)
    printans(ans)
