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

def dfs(k, S, maxlcp, sList):
    nextGroups = dict()
    for i in S:
        if len(sList[i]) == k:
            maxlcp[i] = k
            continue
        c = sList[i][k]
        if c not in nextGroups:
            nextGroups[c] = [i]
        else:
            nextGroups[c].append(i)
    for grp in nextGroups.values():
        if len(grp) == 1:
            maxlcp[grp[0]] = k
            continue
        dfs(k+1, grp, maxlcp, sList)
    return

def solve(n,sList):
    maxlcp = [0 for _ in range(n)]
    S = [i for i in range(n)]
    dfs(0, S, maxlcp, sList)
    return maxlcp

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,sList=readinput()
    ans=solve(n,sList)
    printans(ans)
