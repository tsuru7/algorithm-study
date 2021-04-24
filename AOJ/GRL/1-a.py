from collections import deque

def readinput():
    v, e, r = map(int, input().split())
    nList = []
    for _ in range(v):
        nList.append([])
    for _ in range(e):
        s, t, d = map(int, input().split())
        nList[s].append((t, d))
    return v, e, r, nList

WHITE = 0
GRAY = 1
BLACK = 2
status = None
depth = None
def bfs(u, nList):
    global status
    global depth

    queue = deque()
    queue.append(u)
    status[u] = GRAY
    depth[u] = 0
    while len(queue) > 0:
        u = queue.popleft()
        for v, w in nList[u]:
            if status[v] == WHITE:
                queue.append(v)
                status[v] = GRAY
                depth[v] = depth[u] + w
        status[u] = BLACK

def main(v, e, r, nList):
    global status
    global depth

    status = [WHITE] * v
    depth = [-1] * v
    bfs(r, nList)

    return depth

def printans(ans):
    for d in ans:
        if d != -1:
            print(d)
        else:
            print('INF')

if __name__ == '__main__':
    v, e, r, nList = readinput()
    ans = main(v, e, r, nList)
    printans(ans)
