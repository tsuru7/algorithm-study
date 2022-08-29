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
    p = []
    amat = [ [0 for col in range(w)] for row in range(h) ]
    for _ in range(n):
        r, c, a = m_input()
        r -= 1
        c -= 1
        amat[r][c] = a
        p.append((r,c))
    return h, w, n, amat, p

def main(h, w, n, amat, p):
    nList = [ [] for _ in range(n) ]
    for i in range(n):
        r, c = p[i]
        a = amat[r][c]
        for row in range(h):
            if amat[row][c] > a:
                nList[i].append((row, c))
        for col in range(w):
            if amat[r][col] > a:
                nList[i].append((r, col))
            
    ans = []
    for i in range(n):
        pi = p[i]
        visited = [False]*n
        ans.append(dfs(pi, nList, visited, 0))
    return ans

def dfs(u, nList, visited, count):
    for v in nList[u]:
        if not visited[v]:
            cnt = dfs()

def printans(ans):
    print(ans)

if __name__=='__main__':
    h, w, n, amat, p=readinput()
    ans=main(h, w, n, amat, p)
    printans(ans)
