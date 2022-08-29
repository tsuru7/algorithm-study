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
    n = i_input()
    x = l_input()
    c = l_input()
    return n,x,c

def dfs(i, x, visited, loop_nodes):
    next = x[i]-1
    if visited[next] == 2:
        return -1
    elif visited[next] == 1:
        # print(f'loop_found: {next} at i: {i}')
        loop_nodes.append(i)
        return next

    visited[next] = 1
    loop_head = dfs(next, x, visited, loop_nodes)
    visited[next] = 2
    if loop_head == i:
        loop_nodes.append(i)
        return -1
    elif loop_head != -1:
        loop_nodes.append(i)
    return loop_head

def calc_cost(loop_nodes, c):
    ans = INFTY
    for i in loop_nodes:
        ans = min(ans, c[i])
    return ans

def solve(n,x,c):
    cost = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            loop_nodes = []
            visited[i] = 1
            dfs(i, x, visited, loop_nodes)
            visited[i] = 2
            # print(f'loop_nodes: {loop_nodes}')
            if len(loop_nodes) > 0:
                cost += calc_cost(loop_nodes, c)

    return cost

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,c=readinput()
    ans=solve(n,x,c)
    printans(ans)
