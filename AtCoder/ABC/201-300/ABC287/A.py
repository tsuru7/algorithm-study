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
    n=i_input()
    sList = [input() for _ in range(n)]
    return n,sList

def solve(n,sList):
    count = 0
    for i in range(n):
        if sList[i] == 'For':
            count += 1
    against = n - count
    if count > against:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,sList=readinput()
    ans=solve(n,sList)
    printans(ans)
