from collections import deque

def readinput():
    n = int(input())
    nList = []
    for _ in range(n+1):
        nList.append([])
    
    for _ in range(n):
        l = list(map(int, input().split()))
        u = l[0]
        k = l[1]
        for v in range(k):
            nList[u].append(l[v+2])
        nList[u].append(-1)
    
    return n, nList

WHITE = 0
GRAY = 1
BLACK = 2

def bfs(u, nList, depth, status):
    queue = deque()

    status[u] = GRAY
    depth[u] = 0
    queue.append(u)

    while len(queue) > 0:
        u = queue.popleft()
        # 前処理をここで実行
        for v in nList[u]:
            if v != -1 and status[v] == WHITE:
                status[v] = GRAY
                depth[v] = depth[u] + 1
                queue.append(v)
        # 後処理をここで実行
        status[u] = BLACK

def main(n, nList):
    depth = [-1] * (n+1)
    status = [WHITE] * (n+1)
    bfs(1, nList, depth, status)
    return depth

def printans(ans):
    # print(ans)
    n = len(ans)
    for i in range(1, n):
        print('{} {}'.format(i, ans[i]))

if __name__ == '__main__':
    n, nList = readinput()
    ans = main(n, nList)
    printans(ans) 
