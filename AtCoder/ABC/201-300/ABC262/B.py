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
    n,m=m_input()
    graph = [set() for _ in range(n)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].add(v)
        graph[v].add(u)
    return n,m,graph

def solve(n,m,graph):
    ans=0
    for a in range(n):
        for b in range(a+1, n):
            if not b in graph[a]:
                continue
            for c in range(b+1, n):
                if not c in graph[b] or not c in graph[a]:
                    continue
                ans += 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
