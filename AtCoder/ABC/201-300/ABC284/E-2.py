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
    n,m=m_input()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = m_input()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    return n,m,graph

def solve(n,m,graph):
    total = 0
    visited = [False for _ in range(n)]
    stack = []
    u = 0
    stack.append(~u)
    stack.append(u)
    while len(stack) > 0:
        u = stack.pop()
        if u >= 0:
            # すでに探索済みの場合は帰りがけ順用のエントリもスタックから削除
            if visited[u]:
                stack.pop()
                continue
            # 行きがけ順の処理
            visited[u] = True
            total += 1
            if total >= 10**6:
                return total
            for v in graph[u][::-1]:
                if visited[v]:
                    continue
                stack.append(~v)
                stack.append(v)
        else:
            # 帰りがけ順の処理
            # ここでは頂点 u が ~u となっているので、元に戻すのを忘れない
            visited[~u] = False
    return total

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
