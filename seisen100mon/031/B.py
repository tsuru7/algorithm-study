import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    w,h=m_input()
    amap = [ [0] + l_input() + [0] for _ in range(h) ]
    amap.insert(0, [0]*(w+2))
    amap.append([0]*(w+2))
    return w,h,amap

def next_vertex(u, dir, amap, visited_block):
    row, col, ud = u
    if dir == 'N':
        if row <= 1:
            return None
        if row % 2 == 0:
            if amap[row-1][col-1] ^ amap[row-1][col] == 1:
                visited_block[row-1][col-1] = True
                visited_block[row-1][col] = True
                return (row-2, col, 1)
            else:
                return None
        else:
            if amap[row-1][col] ^ amap[row-1][col+1] == 1:
                visited_block[row-1][col] = True
                visited_block[row-1][col+1] = True
                return (row-2, col, 1)
            else:
                return None

    elif dir == 'S':
        if row >= h:
            return None
        if row % 2 == 0:
            if amap[row+1][col-1] ^ amap[row+1][col] == 1:
                visited_block[row+1][col-1] = True
                visited_block[row+1][col] = True
                return (row+2, col, 0)
            else:
                return None
        else:
            if amap[row+1][col] ^ amap[row+1][col+1] == 1:
                visited_block[row+1][col] = True
                visited_block[row+1][col+1] = True
                return (row+2, col, 0)
            else:
                return None

    elif dir == 'SW':
        if col <= 0:
            return None
        if row % 2 == 0:
            if amap[row][col] ^ amap[row-1][col-1] == 1:
                visited_block[row][col] = True
                visited_block[row-1][col-1] = True
                return (row-1, col-1, 1)
            else:
                return None
        else:
            if amap[row][col] ^ amap[row-1][col] == 1:
                visited_block[row][col] = True
                visited_block[row-1][col] = True
                return (row-1, col, 1)
            else:
                return None

    elif dir == 'SE':
        if col > w:
            return None
        if row % 2 == 0:
            if amap[row][col] ^ amap[row-1][col] == 1:
                visited_block[row][col] = True
                visited_block[row-1][col] = True
                return (row-1, col, 1)
            else:
                return None
        else:
            if amap[row][col] ^ amap[row-1][col+1] == 1:
                visited_block[row][col] = True
                visited_block[row-1][col+1] = True
                return (row-1, col+1, 1)
            else:
                return None

    elif dir == 'NW':
        if col <= 0:
            return None
        if row % 2 == 0:
            if amap[row][col] ^ amap[row+1][col-1] == 1:
                visited_block[row][col] = True
                visited_block[row+1][col-1] = True
                return (row+1, col-1, 0)
            else:
                return None
        else:
            if amap[row][col] ^ amap[row+1][col] == 1:
                visited_block[row][col] = True
                visited_block[row+1][col] = True
                return (row+1, col, 0)
            else:
                return None

    elif dir == 'NE':
        if col > w:
            return None
        if row % 2 == 0:
            if amap[row][col] ^ amap[row+1][col] == 1:
                visited_block[row][col] = True
                visited_block[row+1][col] = True
                return (row+1, col, 0)
            else:
                return None
        else:
            if amap[row][col] ^ amap[row+1][col+1] == 1:
                visited_block[row][col] = True
                visited_block[row+1][col+1] = True
                return (row+1, col+1, 0)
            else:
                return None

def bfs(u, w, h, amap, visited_block):
    edges = set()
    queue = deque()
    visited_vertex = [ [ [False, False] for col in range(w+2) ] for row in range(h+2) ]
    st_row, st_col = u
    start_vertex = (st_row, st_col, 0)
    visited_vertex[st_row][st_col][0] = True
    queue.append(start_vertex)
    while len(queue) > 0:
        u = queue.popleft()
        row, col, ud = u
        if ud == 0:
            # visited_block[row][col] = True
            dirs = ['N', 'SW', 'SE']
        else:
            dirs = ['S', 'NW', 'NE']
        for dir in dirs:
            v = next_vertex(u, dir, amap, visited_block) # 到達できないケースはNoneを返す
            if v is None:
                continue
            row_v, col_v, ud_v = v
            if visited_vertex[row_v][col_v][ud_v]:
                edges.add(tuple(sorted((u,v))))
                continue
            visited_vertex[row_v][col_v][ud_v] = True
            queue.append(v)
            edges.add(tuple(sorted((u, v))))
    print(f'len(edges): {len(edges)}')
    return len(edges)

def solve(w,h,amap):
    ans=0
    visited = [ [False]*(w+2) for _ in range(h+2) ]
    for row in range(1, h+1):
        for col in range(1, w+1):
            if amap[row][col] == 0 or visited[row][col]:
                continue
            print(f'row: {row}, col: {col}')
            ans += bfs((row, col), w, h, amap, visited)
            # print('visited:')
            # print(*visited, sep='\n')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    w,h,amap=readinput()
    ans=solve(w,h,amap)
    printans(ans)
