import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
import copy
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
    smap = []
    for _ in range(10):
        smap.append(input())
    return smap

def dfs(u, nlist, visited):
    visited[u] = True
    if len(nlist[u]) == 0:
        return
    for v in nlist[u]:
        if visited[v]:
            continue
        dfs(v, nlist, visited)
    return

def solve(smap):
    nlist = [[] for _ in range(100)]
    visited = [False]*100
    start_ij = -1
    for row in range(10):
        for col in range(10):
            c = smap[row][col]
            ij = row*10+col
            if c == 'x':
                visited[ij] = True
                continue
            if start_ij == -1:
                start_ij = ij
            if col > 0 and smap[row][col-1] == 'o':
                nlist[ij].append(ij-1)
            if col < 9 and smap[row][col+1] == 'o':
                nlist[ij].append(ij+1)
            if row > 0 and smap[row-1][col] == 'o':
                nlist[ij].append(ij-10)
            if row < 9 and smap[row+1][col] == 'o':
                nlist[ij].append(ij+10)
    
    dfs(start_ij, nlist, visited)

    connected = True
    for ij in range(100):
        if visited[ij] == False:
            connected = False
            break
    return connected

def main(smap):
    if solve(smap):
        return 'YES'


    for row in range(10):
        for col in range(10):
            smap_mod = []
            for s in smap:
                smap_mod.append(list(s))
            if smap_mod[row][col] == 'o':
                continue
            smap_mod[row][col] = 'o'
            # print_smap(smap)
            if solve(smap_mod):
                return 'YES'
    return 'NO'

def print_smap(smap):
    print('--- smap ---')
    for s in smap:
        print(s)

def printans(ans):
    print(ans)

if __name__=='__main__':
    smap=readinput()
    ans=main(smap)
    printans(ans)
