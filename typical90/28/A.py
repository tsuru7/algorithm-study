import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict

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
    n=i_input()
    papers = [l_input() for _ in range(n)]
    return n,papers

def solve(n,papers):
    plane = [[0 for _ in range(1002)] for _ in range(1002)]
    for lx, ly, rx, ry in papers:
        plane[lx][ly] += 1
        plane[rx][ly] -= 1
        plane[lx][ry] -= 1
        plane[rx][ry] += 1
    for y in range(1002):
        for x in range(1001):
            plane[x+1][y] += plane[x][y]
    for x in range(1002):
        for y in range(1001):
            plane[x][y+1] += plane[x][y]

    # for y in range(10):
    #     for x in range(10):
    #         print(plane[x][y], end=' ')
    #     print()
    
    ans=defaultdict(int)
    for x in range(1001):
        for y in range(1001):
            ans[plane[x][y]] += 1
    return ans

def printans(ans):
    for k in range(1, n+1):
        print(ans[k])

if __name__=='__main__':
    n,papers=readinput()
    ans=solve(n,papers)
    printans(ans)
