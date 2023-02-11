import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    a,b=m_input()
    return a,b

def solve(a,b):
    if a == 2*b or a == 2*b + 1:
        return 'Yes'
    if b == 2 * a or b == 2 * a + 1:
        return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=solve(a,b)
    printans(ans)
