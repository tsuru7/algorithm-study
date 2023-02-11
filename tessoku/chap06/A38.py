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
    d,n=m_input()
    limits = [l_input() for _ in range(n)]
    return d,n,limits

def solve(d,n,limits):
    hours = [24 for _ in range(d)]
    for l, r, h in limits:
        l -= 1
        r -= 1
        for i in range(l, r+1):
            hours[i] = min(hours[i], h)
    ans=0
    for i in range(d):
        ans += hours[i]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    d,n,limits=readinput()
    ans=solve(d,n,limits)
    printans(ans)
