import sys
sys.setrecursionlimit(10**7)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,m=m_input()
    nlist = [ [] for _ in range(n)]
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        nlist[a].append(b)
        nlist[b].append(a)
    return n,m,nlist

RED = 1
GREEN = 2
BLUE = 3
color = None
visited = None
def dfs(u, nlist):
    global color
    global visited

    visited[u] = True
    print(f'dfs: {u}', color)
    available = {RED, GREEN, BLUE}  # 自分を塗ることができる色の集合
    # available.remove(color[u]) # 自分の色は除く
    # 自分の周りの頂点の色を調べて available から除く
    unvisited = 0
    for v in nlist[u]:
        if not visited[v]:
            unvisited += 1
        if color[v] != 0 and color[v] in available:
            available.remove(color[v])
    print(available)
    if unvisited == 0:
        color[u] = 4
        return len(available)

    count = 0
    for c in available:  # 自分を塗ることができる色を変えながら繰り返す
        color[u] = c
        for v in nlist[u]:
            if color[v] == 0:  # まだ塗っていない頂点について再帰的に呼び出す
                count *= dfs(v, nlist)
    color[u] = 0
    print(f'dfs return: {count}')
    return count

def main(n,m,nlist):
    global color
    global visited

    color = [0]*n
    visited = [False]*n
    counts = []
    for i in range(n):
        if color[i] == 0:
            # color[0] = RED
            counts.append(dfs(i, nlist))
    print(counts)
    ans = 1
    for count in counts:
        ans *= count

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,nlist=readinput()
    ans=main(n,m,nlist)
    printans(ans)
