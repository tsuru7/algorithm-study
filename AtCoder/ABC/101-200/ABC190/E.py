def readinput():
    n,m=map(int,input().split())
    nList = []
    for _ in range(n+1):
        nList.append([])
    for _ in range(m):
        a, b = map(int, input().split())
        nList[a].append(b)
        nList[b].append(a)
    k = int(input())
    c=list(map(int,input().split()))
    return n,m,nList,k,c

import sys
INFTY=sys.maxsize
def main(n,m,nList,k,c):
    global status

    cSet = set(c)
    for i in range(1, n+1):
        nList[i] = list(set(nList[i]) - cset)
    minpathlen=INFTY

    status = [WHITE]*(n+1)
    for u in c:
        pathlen = dfs(u, nList)
        minpathlen=min(minpathlen, pathlen)
    return minpathlen

WHITE=0
GRAY=1
BLACK=2
status=None
from collections import deque
def dfs(u, nList):
    global status

    queue = deque()
    queue.append(u):
    time_ = 0
    while len(u) > 0:
        u = queue[-1]
        v = next[u]
        if v != -1:
            if status[v] == WHITE:
                queue.append(v)
                status[v] = GRAY
        else:
            queue.pop()

        

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,nList,k,c=readinput()
    ans=main(n,m,nList,k,c)
    printans(ans)
