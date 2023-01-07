import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
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
    n,m,b=m_input()
    a=l_input()
    c = l_input()
    return n,m,a,b,c

def solve(n,m,a,b,c):
    suma = sum(a)
    sumc = sum(c)
    ans = suma * m + sumc * n + b * m * n
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a,b,c=readinput()
    ans=solve(n,m,a,b,c)
    printans(ans)
