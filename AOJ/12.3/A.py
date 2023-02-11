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
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        tmp = l_input()
        u = tmp[0]
        nv = tmp[1]
        if nv > 0:
            for v in tmp[2:]:
                graph[u].append(v)
    return n,graph

def solve(n,graph):
    visited = [False for _ in range(n+1)]
    find = [0 for _ in range(n+1)]
    comp = [0 for _ in range(n+1)]
    stack = []
    time_ = 0
    for i in range(1, n+1):
        if visited[i]:
            continue
        u = i
        stack.append(~u)
        stack.append(u)
        while len(stack) > 0:
            u = stack.pop()
            if u >= 0:
                if visited[u]:
                    stack.pop()
                    continue
                # 行きがけ順の処理
                visited[u] = True
                time_ += 1
                find[u] = time_
                for v in graph[u][::-1]:
                    if visited[v]:
                        continue
                    stack.append(~v)
                    stack.append(v)
            else:
                time_ += 1
                comp[~u] = time_
    ans = []
    for i in range(1, n+1):
        ans.append((i, find[i], comp[i]))
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,graph=readinput()
    ans=solve(n,graph)
    printans(ans)
