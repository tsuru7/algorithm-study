import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    lrList.sort()
    cum = [[0 for j in range(m)] for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            cum[i][j] = cum[i][j-1] if j-1 >= 0 else 0
            l, r = lrList[j]
            l -= 1
            r -= 1
            if l <= i <= r:
                cum[i][j] += 1
    ans=[]
    for p, q in queries:
        l = bisect_left(lrList, [p, 0])
        r = bisect_left(lrList, [q+1, 0])
        # print(f'p: {p}, q: {q}, l: {l}, r: {r}')
        # if r == m:
        #     r -= 1
        if l-1 >= 0:
            rest = cum[q][r-1]-cum[q][l-1]
        else:
            rest = cum[q][r-1]
        ans.append(r-l - rest)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,q,lrList,queries=readinput()
    ans=solve(n,m,q,lrList,queries)
    printans(ans)
