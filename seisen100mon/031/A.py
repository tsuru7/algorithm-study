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

def judge(u, amap, dir):
    x, y, z = u
    if dir == 'N':
        if y % 2 == 0:
            if amap[x-1][y-1] ^ amap[x][y-1] == 1:
                return True
            else:
                return False
        else:
            if amap[x][y-1] ^ amap[x+1][y-1] == 1:
                return True
            else:
                return False
    elif dir == 'S':
        if y % 2 == 0:
            if amap[x-1][y+1] ^ amap[x][y+1] == 1:
                return True
            else:
                return False
        else:
            if amap[x][y+1] ^ amap[x+1][y+1] == 1:
                return True
            else:
                return False
    elif dir == 'NW':
        if y % 2 == 0:
            if amap[x-1][y] ^ amap[x-1][y-1] == 1:
                return True
            else:
                return False
        else:
            if amap[x-1][y] ^ amap[x][y-1] == 1:
                return True
            else:
                return False
    elif dir == 'NE':
        if y % 2 == 0:
            if amap[x+1]

def gen_v(u, dir):
    x, y, z = u
    if dir == 'N':
        return (x, y-2, 1)
    elif dir == 'S':
        return (x, y+2, 0)
    elif dir == 'NW':
        if y % 2 == 0:
            return (x-1, y-1, 1)
        else:
            return (x, y-1, 1)
    elif dir == 'NE':
        if y % 2 == 0:
            return (x, y-1, 1)
        else:
            return (x+1, y-1, 1)
    elif dir == 'SW':
        if y % 2 == 0:
            return (x-1, y+1, 0)
        else:
            return (x, y+1, 0)
    elif dir == 'SE':
        if y % 2 == 0:
            return (x, y+1, 0)
        else:
            return (x+1, y+1, 0)

def edge_bfs(block_row, block_col, w,h,amap, visited_block):
    queue = deque()
    painted = set()
    u = (block_row, block_col, 0)
    queue.append(u)
    visited = [ [ [False, False] for col in range(w+2) ] for row in range(h+2) ]
    visited[block_row][block_col][0] = True
    while len(queue) > 0:
        x, y, z = queue.popleft()
        if z == 0:
            dirs = ['N', 'SW', 'SE']
            visited_block[]
        else:
            dirs = ['S', 'NW', 'NE']

        for dir in dirs:
            v = gen_v(u, dir)
            r, s, t = v
            if r < 0 or r > w+1 or s < 0 or s > h+1:
                continue
            if visited[r][s][t]:
                painted.add(sorted([u, v]))
                continue
            if judge(u, amap, dir):
                visited[r][s][t] = True
                painted.add(sorted([u, v]))
                queue.append(v)

    return len(painted)

def solve(w,h,amap):
    ans = 0
    visited_block = [ [False]*(w+2) for _ in range(h+2) ]
    for row in range(1, h+1):
        for col in range(1, w+1):
            if visited_block[row][col]:
                continue
            ans += edge_bfs(row, col, w, h, amap, visited_block)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    w,h,amap=readinput()
    ans=solve(w,h,amap)
    printans(ans)
