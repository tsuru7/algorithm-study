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
    n,m=m_input()
    sList = [input() for _ in range(n)]
    tList = [input() for _ in range(m)]
    return n,m,sList,tList

def solve(n,m,sList,tList):
    ans=0
    for i in range(n):
        si = sList[i]
        for j in range(m):
            tj = tList[j]
            if si[-3:] == tj:
                ans += 1
                break
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,sList,tList=readinput()
    ans=solve(n,m,sList,tList)
    printans(ans)
