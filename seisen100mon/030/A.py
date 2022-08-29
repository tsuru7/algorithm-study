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
    h,w,n=m_input()
    cmap = [ input() for _ in range(h) ]
    return h,w,n,cmap

def solve(h,w,n,cmap):
    goals = dict()
    for row in range(h):
        for col in range(w):
            if cmap[row][col] == 'S':
                start = (row, col)
            elif cmap[row][col] not in ['X', '.']:
                goals[cmap[row][col]] = (row, col)
    # print(f'start: {start}, goals: {goals}')
    ans=0
    u = start
    for target in range(1, n+1):
        queue = deque()
        queue.append(u)
        visited = [ [-1]*w for _ in range(h) ]
        visited[u[0]][u[1]] = 0
        while len(queue) > 0:
            row, col = queue.popleft()
            if (row, col) == goals[str(target)]:
                ans += visited[row][col]
                u = (row, col)
                break
            for dr,dc in [ (-1,0), (1,0), (0,-1), (0,1) ]:
                if 0 <= row+dr < h and 0 <= col+dc < w and cmap[row+dr][col+dc] != 'X':
                    if visited[row+dr][col+dc] == -1:
                        queue.append((row+dr, col+dc))
                        visited[row+dr][col+dc] = visited[row][col] + 1
            # print(f'queue: {queue}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,n,cmap=readinput()
    ans=solve(h,w,n,cmap)
    printans(ans)
