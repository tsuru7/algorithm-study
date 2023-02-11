from collections import deque

def readinput():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    cmap = []
    for _ in range(r):
        cmap.append(input())
    return r,c, sx, sy, gx, gy, cmap

WHITE = 0
GRAY = 1
BLACK = 2
status = None
depth = None
def bfs(s, nList, g):
    global status
    global depth

    queue = deque()
    u = s
    depth[u] = 0
    queue.append(u)
    status[u] = GRAY
    while len(queue) > 0:
        # print(queue)
        u = queue.popleft()
        for v in nList[u]:
            if status[v] == WHITE:
                queue.append(v)
                status[v] = GRAY
                depth[v] = depth[u] + 1
                if v == g:
                    return depth[v]
        status[u] = BLACK
    return 0

def main(r,c, sx, sy, gx, gy, cmap):
    global status
    global depth

    # def ij(n):
    #     return (n//c, n%c)

    def n(i, j):
        return i*c+j

    nList = []
    for _ in range(c*r):
        nList.append([])
    for i in range(r):
        for j in range(c):
            m = n(i, j)
            if cmap[i][j] == '.':
                if i > 0 and cmap[i-1][j] == '.':
                    nList[m].append(n(i-1, j))
                if i < r and cmap[i+1][j] == '.':
                    nList[m].append(n(i+1, j))
                if j > 0 and cmap[i][j-1] == '.':
                    nList[m].append(n(i, j-1))
                if j < c and cmap[i][j+1] == '.':
                    nList[m].append(n(i, j+1))
    # printList(nList)
    status = [WHITE] * (c*r)
    depth = [-1] * (c*r)

    # print('s: ', n(sy-1, sx-1))
    # print('g: ', n(gy-1, gx-1))
    d = bfs(n(sy-1, sx-1), nList, n(gy-1, gx-1))

    return d

def printList(l):
    for idx, ll in enumerate(l):
        print(idx, ll)

def printans(ans):
    print(ans)

if __name__ == '__main__':
    r,c, sx, sy, gx, gy, cmap = readinput()
    ans = main(r,c, sx, sy, gx, gy, cmap)
    printans(ans)
