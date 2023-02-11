import sys
sys.setrecursionlimit(10**5)
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
    n=i_input()
    a=l_input()
    return n,a

def bfs(u, nList, visited):
    queue = deque()
    queue.append(u)
    visited[u] = True
    count = 1
    while len(queue) > 0:
        u = queue.popleft()
        for v in nList[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                count += 1
    return count

def main(n,a):
    nList = []
    for _ in range(2*10**5):
        nList.append([])
    for i in range(n):
        if a[i] != a[n-1-i]:
            nList[a[i]-1].append(a[n-1-i]-1)
            nList[a[n-1-i]-1].append(a[i]-1)
    visited = [False]*(2*10**5)
    count = 0
    for i in range(2*10**5):
        if not visited[i]:
            count += bfs(i, nList, visited) - 1

    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
