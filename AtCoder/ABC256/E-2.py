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
    x = l_input()
    c = l_input()
    return n,x,c

def dfs(u, x, visited, loop):
    visited[u] = 1
    next = x[u]
    if visited[next] == 2:
        visited[u] = 2
        return -1
    if visited[next] == 1:
        loop.append(u)
        visited[u] = 2
        return next
    if visited[next] == -1:
        tmp = dfs(next, x, visited, loop)
        if tmp == u:
            loop.append(u)
            visited[u] = 2
            return -1
        if tmp != -1:
            loop.append(u)
            visited[u] = 2
            return tmp
        visited[u] = 2
        return -1

def calc_cost(i, x, c, visited):
    loop = []
    dfs(i, x, visited, loop)
    if len(loop) == 0:
        return 0
    cost = INFTY
    for i in loop:
        cost = min(cost, c[i])
    return cost

def solve(n,x,c):
    visited = [-1 for _ in range(n)]
    x = [x[i]-1 for i in range(n)]
    cost = 0
    for i in range(n):
        if visited[i] == -1:
            cost += calc_cost(i, x, c, visited)
    return cost

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,c=readinput()
    ans=solve(n,x,c)
    printans(ans)
