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
    w, h = m_input()
    maze = []
    while w != 0 or h != 0:
        tate = []
        yoko = []
        for i in range(2*h-1):
            if i % 2 == 0:
                tate.append(l_input())
            else:
                yoko.append(l_input())
        maze.append((w, h, tate, yoko))
        w, h = m_input()
    return maze

def solve(maze):
    ans=[]
    for w, h, tate, yoko in maze:
        # print(f'w: {w}, {h}, tate: {tate}, yoko: {yoko}')
        visited = [ [-1]*w for _ in range(h) ]
        queue = deque()
        u = (0, 0)
        visited[0][0] = 1
        queue.append(u)
        while len(queue) > 0:
            # print(f'queue: {queue}')
            row, col = queue.popleft()
            # 上
            dr, dc = -1, 0
            if 0 <= row+dr < h and 0 <= col+dc < w and visited[row+dr][col+dc] < 0:
                if yoko[row-1][col] == 0:
                    visited[row+dr][col+dc] = visited[row][col] + 1
                    v = (row+dr, col+dc)
                    queue.append(v)
            # 下
            dr, dc = 1, 0
            if 0 <= row+dr < h and 0 <= col+dc < w and visited[row+dr][col+dc] < 0:
                if yoko[row][col] == 0:
                    visited[row+dr][col+dc] = visited[row][col] + 1
                    v = (row+dr, col+dc)
                    queue.append(v)
            # 左
            dr, dc = 0, -1
            if 0 <= row+dr < h and 0 <= col+dc < w and visited[row+dr][col+dc] < 0:
                if tate[row][col-1] == 0:
                    visited[row+dr][col+dc] = visited[row][col] + 1
                    v = (row+dr, col+dc)
                    queue.append(v)
            # 右
            dr, dc = 0, 1
            # print(f'row+dr: {row+dr}, col+dc: {col+dc}, visited[row+dr][col+dc]: {visited[row+dr][col+dc]}')
            if 0 <= row+dr < h and 0 <= col+dc < w and visited[row+dr][col+dc] < 0:
                # print(f'row: {row}, col: {col}, tate[row][col]: {tate[row][col]}')
                if tate[row][col] == 0:
                    visited[row+dr][col+dc] = visited[row][col] + 1
                    v = (row+dr, col+dc)
                    queue.append(v)
        # print(f'visited: {visited}')
        ans.append(visited[h-1][w-1] if visited[h-1][w-1] != -1 else 0)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    maze=readinput()
    ans=solve(maze)
    printans(ans)
