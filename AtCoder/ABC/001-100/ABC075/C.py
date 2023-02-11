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

def readinput():
    n, m = m_input()
    ab = []
    for _ in range(m):
        ab.append(list(m_input()))
    return n,m,ab

visited = None
WHITE = 0
GRAY = 1
BLACK = 2
def bfs(u, nlist):
    global visited

    queue = deque()
    queue.append(u)
    while len(queue) > 0:
        u = queue.popleft()
        for v in nlist[u]:
            if visited[v] == WHITE:
                queue.append(v)
                visited[v] = GRAY
        visited[u] = BLACK
        

def main(n,m,ab):
    global visited

    ans=0
    for i in range(m):
        nlist = [ [] for _ in range(n) ]
        for j in range(m):
            if j == i:
                continue
            a, b = ab[j]
            a -= 1
            b -= 1
            nlist[a].append(b)
            nlist[b].append(a)
        visited = [WHITE]*n
        groups = 0
        for j in range(n):
            if visited[j] == WHITE:
                groups += 1
                if groups > 1:
                    ans += 1
                    break
                bfs(j, nlist)
        

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,ab=readinput()
    ans=main(n,m,ab)
    printans(ans)
