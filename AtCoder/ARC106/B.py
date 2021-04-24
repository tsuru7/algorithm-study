from collections import deque

def readinput():
    n, m = map(int, input().split())
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))
    nList = []
    for _ in range(n+1):
        nList.append([])
    for _ in range(m):
        c, d = map(int, input().split())
        nList[c].append(d)
        nList[d].append(c)
    return n, m, aList, bList, nList

WHITE = 0
GRAY = 1
BLACK = 2
status = None
def bfs(u, nList):
    global status

    sameList = []
    queue = deque()
    queue.append(u)
    status[u] = GRAY
    while len(queue) > 0:
        u = queue.popleft()
        for v in nList[u]:
            if status[v] == WHITE:
                queue.append(v)
                status[v] = GRAY
        status[u] = BLACK
        sameList.append(u)
    return sameList
    

def main(n, m, aList, bList, nList):
    global status

    status = [WHITE] * (n+1)

    for u in range(1, n+1):
        if status[u] == WHITE:
            sameList = bfs(u, nList)
            suma = 0
            sumb = 0
            for v in sameList:
                suma += aList[v-1]
                sumb += bList[v-1]
            if suma != sumb:
                return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, m, aList, bList, nList = readinput()
    ans = main(n, m, aList, bList, nList)
    printans(ans)
