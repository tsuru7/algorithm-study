from collections import deque

def readinput():
    h, w = map(int, input().split())
    smap = []
    for _ in range(h):
        smap.append(input())
    return h, w, smap

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
        for v in nList[u]:
            if status[v] == WHITE:
                status[v] = GRAY
                queue.append(v)
                depth[v] = depth[u] + 1
        status[u] = BLACK

def getNList(h, w, smap):
    def ij(i, j):
        return i * w + j
    nList = []
    for _ in range(h*w+1):
        nList.append([])
    for i in range(h):
        for j in range(w):
            if smap[i][j] == '#':
                continue
            if i > 0:
                if smap[i-1][j] == '.':
                    nList[ij(i, j)].append(ij(i-1, j))
            if i < h-1:
                if smap[i+1][j] == '.':
                    nList[ij(i, j)].append(ij(i+1, j))
            if j > 0:
                if smap[i][j-1] == '.':
                    nList[ij(i, j)].append(ij(i, j-1))
            if j < w-1:
                if smap[i][j+1] == '.':
                    nList[ij(i, j)].append(ij(i, j+1))
    return nList

def main(h, w, smap):
    global status
    global depth

    def ij(i, j):
        return i * w + j

    if smap[0][0] == '#' or smap[h-1][w-1] == '#':
        return -1

    nwhite = 0
    for i in range(h):
        for j in range(w):
            if smap[i][j] == '.':
                nwhite += 1
    
    nList = getNList(h, w, smap)
    status = [WHITE] * (h*w)
    depth = [-1] * (h*w)
    u = 0
    bfs(u, nList)
    if depth[h*w-1] == -1:
        return -1
    else:
        return nwhite - depth[h*w-1] -1

def printans(ans):
    print(ans)

if __name__ == '__main__':
    h, w, smap = readinput()
    ans = main(h, w, smap)
    printans(ans)
