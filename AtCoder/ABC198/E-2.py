from collections import deque
import sys
sys.setrecursionlimit(10**5)

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    c = l_input()
    nList = []
    for _ in range(n):
        nList.append([])
    for _ in range(n-1):
        a,b=m_input()
        nList[a-1].append(b-1)
        nList[b-1].append(a-1)
    return n,c,nList

WHITE = 0
GRAY = 1
BLACK = 2
BAD = 3
status = None
colors = None
def dfs(nList, u, c):
    global status
    global colors

    status[u] = GRAY
    colors[c[u]-1] += 1
    if colors[c[u]-1] > 1:
        status[u] = BAD

    for v in nList[u]:
        if status[v] == WHITE:
            status[v] = GRAY
            dfs(nList, v, c)
    if status[u] != BAD:
        status[u] = BLACK

    colors[c[u]-1] -= 1
    return


def main(n,c,nList):
    global status
    global colors

    status = [WHITE]*n
    colors = [0]*10**5
    dfs(nList, 0, c)
    ans = []
    for i in range(n):
        if status[i] == BLACK:
            ans.append(i+1)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,c,nList=readinput()
    ans=main(n,c,nList)
    printans(ans)
