import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
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

def print_visited(visited):
    ij = 0
    for _ in range(10):
        print(ij//10, visited[ij:ij+10])
        ij += 10

def print_nlist(nlist):
    for i, l in enumerate(nlist):
        print(f'{i} ({i//10}, {i%10}): {l}')

def main(smap):

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
    
    # print('--- initial ---')
    # print_nlist(nlist)
    # print_visited(visited)

    nlist_work = nlist.copy()
    visited_work = visited.copy()
    dfs(start_ij, nlist_work, visited_work)

    # print('--- no additional land ---')
    # print_visited(visited_work)

    connected = True
    for ij in range(100):
        if visited_work[ij] == False:
            connected = False
            break
    if connected:
        return 'YES'

    for row in range(10):
        # if row != 5:
        #     continue
        for col in range(10):
            # if col != 4:
            #     continue
            if smap[row][col] == 'o':
                continue
            nlist_work = nlist.copy()
            visited_work = visited.copy()
            ij = row*10 + col
            if col > 0 and smap[row][col-1] == 'o':
                nlist_work[ij].append(ij-1)
                nlist_work[ij-1].append(ij)
            if col < 9 and smap[row][col+1] == 'o':
                nlist_work[ij].append(ij+1)
                nlist_work[ij+1].append(ij)
            if row > 0 and smap[row-1][col] == 'o':
                nlist_work[ij].append(ij-10)
                nlist_work[ij-10].append(ij)
            if row < 9 and smap[row+1][col] == 'o':
                nlist_work[ij].append(ij+10)
                nlist_work[ij+10].append(ij)
            visited_work[ij] = False
            dfs(start_ij, nlist_work, visited_work)

            # print(f'--- additional land ({row}, {col}) ---')
            # print_nlist(nlist_work)
            # print_visited(visited_work)

            connected = True
            for ij in range(100):
                if visited_work[ij] == False:
                    connected = False
                    break
            if connected:
                return 'YES'
    return 'NO'

def printans(ans):
    print(ans)

if __name__=='__main__':
    smap=readinput()
    ans=main(smap)
    printans(ans)
