from collections import deque

def readinput():
    n, m = map(int, input().split())
    nList = []
    for _ in range(n+1):
        nList.append([])
    pairs = set()
    for _ in range(m):
        a, b = map(int, input().split())
        if (a, b) in pairs or (b, a) in pairs:
            continue
        nList[a].append(b)
        nList[b].append(a)
        pairs.add((a, b))
        
    return n, nList

WHITE = 0
GRAY = 1
BLACK = 2
status = []
def bfs(u, nList):
    global status

    queue = deque()
    count = 0
    status[u] = GRAY
    queue.append(u)

    while len(queue) > 0:
        u = queue.popleft()
        for v in nList[u]:
            if status[v] == WHITE:
                queue.append(v)
                status[v] = GRAY
        status[u] = BLACK
        count += 1

    return count


def main(n, nList):
    global status
    global next

    status = [WHITE] * (n+1)
    next = [0] * (n+1)

    maxcount = 0
    for u in range(1, n+1):
        count = 0
        if status[u] == WHITE:
            count = bfs(u, nList)
            # print('count={}'.format(count))
            maxcount = max(maxcount, count)

    return maxcount

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, nList = readinput()
    ans = main(n, nList)
    printans(ans)
