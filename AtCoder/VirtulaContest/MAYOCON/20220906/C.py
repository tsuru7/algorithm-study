import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

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
    n,q=m_input()
    queries = [l_input() for _ in range(q)]
    return n,q,queries

def solve(n,q,queries):
    pre = [-1 for _ in range(n)]
    nex = [-1 for _ in range(n)]
    ans=[]
    for query in queries:
        if query[0] == 1:
            x, y = query[1:]
            x -= 1
            y -= 1
            nex[x] = y
            pre[y] = x
        elif query[0] == 2:
            x, y = query[1:]
            x -= 1
            y -= 1
            nex[x] = -1
            pre[y] = -1
        else:
            x = query[1]
            x -= 1
            train = deque()
            now = x
            while pre[now] != -1:
                train.appendleft(pre[now])
                now = pre[now]
            train.append(x)
            now = x
            while nex[now] != -1:
                train.append(nex[now])
                now = nex[now]
            ans.append(list(train))
    return ans

def printans(ans):
    for a in ans:
        tmp = [len(a)] + [i+1 for i in a]
        print(*tmp)

if __name__=='__main__':
    n,q,queries=readinput()
    ans=solve(n,q,queries)
    printans(ans)
