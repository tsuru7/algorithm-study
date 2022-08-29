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
    n,m,q=m_input()
    lrList = [l_input() for _ in range(m)]
    queries = [l_input() for _ in range(q)]
    return n,m,q,lrList,queries

def solve(n,m,q,lrList,queries):
    xmap = [[0 for i in range(n)] for j in range(n)]
    for l, r in lrList:
        l -= 1
        r -= 1
        xmap[l][r] += 1
    cmap = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            cmap[i][j] = (cmap[i][j-1] if j-1 >= 0 else 0) + xmap[i][j]
    ans=[]
    for p, q in queries:
        p -= 1
        q -= 1
        tmp = 0
        for s in range(p, q+1):
            tmp += cmap[s][q]
        ans.append(tmp)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,q,lrList,queries=readinput()
    ans=solve(n,m,q,lrList,queries)
    printans(ans)
