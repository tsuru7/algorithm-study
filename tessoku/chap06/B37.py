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
    n=i_input()
    return n

def f2(k):
    return 45 * k * 10**(k-1)

def f3(k, d):
    sumd = d*(d+1)//2
    return sumd * f2(k-1)

def solve(n):
    keta = len(str(n))
    ans=0
    d = n // 10**(keta-1)
    ans += f3(keta, d-1)
    

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
