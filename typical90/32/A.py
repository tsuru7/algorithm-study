import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations

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
    amat = [l_input() for _ in range(n)]
    m = i_input()
    graph = [set() for _ in range(n)]
    for _ in range(m):
        x, y = m_input()
        x -= 1
        y -= 1
        graph[x].add(y)
        graph[y].add(x)
    return n,amat,m,graph

def solve(n,amat,m,graph):
    ans=INFTY
    for p in permutations(range(n), n):
        now = p[0]
        time = amat[now][0]
        for i in range(1, n):
            next = p[i]
            if next in graph[now]:
                time = INFTY
                break
            time += amat[next][i]
            now = next
        ans = min(ans, time)
    if ans == INFTY:
        return -1
    else:
        return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,amat,m,graph=readinput()
    ans=solve(n,amat,m,graph)
    printans(ans)
