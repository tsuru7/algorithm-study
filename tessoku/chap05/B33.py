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
    n,h,w=m_input()
    abList = [l_input() for _ in range(n)]
    return n,h,w,abList

def solve(n,h,w,abList):
    ans=0
    for i in range(n):
        ai, bi = abList[i]
        ans ^= (ai-1)
        ans ^= (bi-1)
    if ans != 0:
        return 'First'
    else:
        return 'Second'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,h,w,abList=readinput()
    ans=solve(n,h,w,abList)
    printans(ans)
