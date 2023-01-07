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

def solve(n,x,y,a):
    maxa = max(a)
    grundy = [0 for _ in range(maxa+1)]
    for i in range(maxa+1):
        nextset = set()
        if i-x >= 0:
            nextset.add(grundy[i-x])
        if i-y >= 0:
            nextset.add(grundy[i-y])
        candidate = {0, 1, 2} - nextset
        grundy[i] = sorted(list(candidate))[0]

    ans = 0
    for i in range(n):
        ans ^= grundy[a[i]]
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
