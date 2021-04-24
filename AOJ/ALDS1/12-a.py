import sys
INFTY = sys.maxsize

def readinput():
    n = int(input())
    nMap = []
    for _ in range(n):
        nMap.append(list(map(int, input().split())))
    # nList = []
    # for _ in range(n):
    #     nList.append([])
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if nMap[i][j] != -1:
    #             nList[i].append((j, nMap[i][j]))
    #             nList[j].append((i, nMap[i][j]))
    return n, nMap # nList

WHITE = 0
GRAY = 1
BLACK = 2
status = None
parent = None
dist = None
def prim(nMap):
    global status
    global parent
    global dist

    dist[0] = 0
    parent[0] = -1
    cost = 0
    while True:
        mincost = INFTY
        for i in range(n):
            if status[i] != BLACK and dist[i] < mincost:
                mincost = dist[i]
                u = i
        
        if mincost == INFTY:
            break

        status[u] = BLACK
        cost += dist[u]

        for v in range(n):
            if status[v] != BLACK and nMap[u][v] != -1:
                if nMap[u][v] < dist[v]:
                    dist[v] = nMap[u][v]
                    parent[v] = u
                    status[v] = GRAY
    return cost

def main(n, nMap):
    global status
    global parent
    global dist

    status = [WHITE] * n
    parent = [-1] * n
    dist = [INFTY] * n

    cost = prim(nMap)

    return cost

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, nMap = readinput()
    ans = main(n, nMap)
    printans(ans)
