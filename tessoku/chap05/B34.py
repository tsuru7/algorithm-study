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
    n,x,y=m_input()
    a=l_input()
    return n,x,y,a

def grundy(x):
    x %= 5
    if x == 0 or x == 1:
        return 0
    elif x == 2 or x == 3:
        return 1
    else:
        return 2

def solve(n,x,y,a):
    assert x == 2
    assert y == 3

    ans=0
    for i in range(n):
        ans ^= grundy(a[i])
    if ans != 0:
        return 'First'
    else:
        return 'Second'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,a=readinput()
    ans=solve(n,x,y,a)
    printans(ans)
