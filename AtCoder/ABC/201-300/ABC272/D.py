import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right
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
    n,m=m_input()
    return n,m

def solve(n,m):
    # sq: 平方数の集合
    sq = set()
    i = 0
    while i*i <= m:
        sq.add(i*i)
        i += 1
    
    # print(f'sq: {sq}')

    sqlist = list(sq)
    sqlist.sort()
    # x**2+y**2 = Mとなる(x**2, y**2)の組を求める
    x2y2 = set()
    x = 0
    while x*x <= m:
        y2 = m - x*x
        if y2 in sq:
            y = bisect_right(sqlist, y2)
            x2y2.add((x,y-1))
        x += 1

    # print(f'x2y2: {x2y2}')

    dist = [-1 for _ in range(n*n)]
    srow = 0
    scol = 0
    dist[srow*n+scol] = 0
    queue = deque()
    queue.append((srow, scol))
    while len(queue) > 0:
        urow, ucol = queue.popleft()
        for x, y in x2y2:
            for vrow, vcol in [(urow+x, ucol+y), (urow+x, ucol-y), (urow-x, ucol+y), (urow-x, ucol-y)]:
                if 0 <= vrow < n and 0 <= vcol < n and dist[vrow*n+vcol] == -1:
                    dist[vrow*n+vcol] = dist[urow*n+ucol] + 1
                    queue.append((vrow, vcol))
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            ans[row][col] = dist[row*n+col]
    return ans 

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,m=readinput()
    ans=solve(n,m)
    printans(ans)
