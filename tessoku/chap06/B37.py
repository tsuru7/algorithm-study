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

def solve(n):
    n = str(n)
    keta = len(n)
    dp_smaller = [0 for _ in range(keta+1)]
    dp_onhold = [0 for _ in range(keta+1)]
    for i in range(keta):
        di = int(n[i])
        Di = int(n[:i]) if i > 0 else 0
        dp_smaller[i+1] += dp_smaller[i]*10 + Di*45
        dp_smaller[i+1] += dp_onhold[i]*di + (di-1)*di//2
        dp_onhold[i+1] += dp_onhold[i] + di
    return dp_smaller[keta] + dp_onhold[keta]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
