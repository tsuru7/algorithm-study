from collections import deque

def readinput():
    n, q = map(int, input().split())
    nList = []
    for _ in range(n+1):
        nList.append([])
    for _ in range(n-1):
        a, b = map(int, input().split())
        nList[a].append(b)
        nList[b].append(a)
    counter = [0] * (n+1)
    for _ in range(q):
        p, x = map(int, input().split())
        counter[p] += x
    
    return n, nList, counter

WHITE = 0
GRAY = 1
BLACK = 2
def bfs(u, nList, counter):
    n = len(nList)
    status = [WHITE] * n

    queue = deque()
    
    status[u] = GRAY
    queue.append(u)

    while len(queue) > 0:
        u = queue.popleft()
        for v in nList[u]:
            if status[v] == WHITE:
                status[v] = GRAY
                counter[v] += counter[u]
                queue.append(v)
        status[u] = BLACK

def main(n, nList, counter):
    bfs(1, nList, counter)
    return counter[1:]

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    n, nList, counter = readinput()
    ans = main(n, nList, counter)
    printans(ans)
