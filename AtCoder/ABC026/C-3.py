import sys
sys.setrecursionlimit(10**5)
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
    graph = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        b = i_input()
        graph[i].append(b)
        graph[b].append(i)
    return n,graph

def dfs(u, graph):
    if u != 1 and len(graph[u]) == 1:  # 隣接ノードが親だけの場合
        return 1

    max_sarary = 0
    min_sarary = INFTY
    for v in graph[u]:
        if v < u:
            continue
        tmp_sarary = dfs(v, graph)
        max_sarary = max(max_sarary, tmp_sarary)
        min_sarary = min(min_sarary, tmp_sarary)
    return max_sarary + min_sarary + 1

def main(n,graph):
    ans=dfs(1, graph)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,graph=readinput()
    ans=main(n,graph)
    printans(ans)
