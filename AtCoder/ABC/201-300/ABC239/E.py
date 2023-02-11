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
    n,q=m_input()
    x=l_input()
    graph = [ [] for _ in range(n) ]
    for _ in range(n-1):
        a, b = m_input()
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    vklist = [l_input() for _ in range(q)]
    return n,q,x,graph,vklist

max20list = None
visited = None
def solve(n,q,x,graph,vklist):
    global max20list
    global visited

    max20list = [ [] for _ in range(n) ]
    visited = [False]*n

    u = 0
    visited[u] = True
    get_max20(u, x, graph)
    
    # print(f'max20list: {max20list}')

    ans = []
    for v, k in vklist:
        v -= 1
        k -= 1
        ans.append(max20list[v][k])
    return ans

def get_max20(u, x, graph):
    global visited
    global max20list

    max20 = [x[u]]
    # print(f'max20: {max20}')

    for v in graph[u]:
        if visited[v]:
            continue
        visited[v] = True
        max20 += get_max20(v, x, graph)
    max20.sort(reverse=True)
    max20list[u] = max20[:20]
    # print(f'u: {u+1}, max20: {max20}')
    return max20[:20]

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,x,graph,vklist=readinput()

    # print(f'graph: {graph}')
    # print(f'vklist: {vklist}')

    ans=solve(n,q,x,graph,vklist)
    printans(ans)
