import sys
sys.setrecursionlimit(10**6)
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
    cpList = [l_input() for _ in range(n)]
    q = i_input()
    lrList = [l_input() for _ in range(q)]
    return n,cpList,q,lrList

def solve(n,cpList,q,lrList):
    cum1 = [0 for _ in range(n+1)]
    cum2 = [0 for _ in range(n+1)]
    for i in range(n):
        ci, pi = cpList[i]
        if ci == 1:
            cum1[i+1] += cum1[i] + pi
            cum2[i+1] = cum2[i]
        else:
            cum1[i+1] = cum1[i]
            cum2[i+1] = cum2[i] + pi
    ans=[]
    for l, r in lrList:
        ans.append((cum1[r]-cum1[l-1], cum2[r]-cum2[l-1]))
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,cpList,q,lrList=readinput()
    ans=solve(n,cpList,q,lrList)
    printans(ans)
