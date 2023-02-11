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
    alist = []
    for i in range(4):
        alist += l_input()
    return alist

def main(alist):
    # bfsする際の先頭ノード(村のある場所)を探す
    head = 0
    for i in range(16):
        if alist[i] == 1:
            head = i
            break

    ans=0
    # 消すマスの組み合わせを全探索
    for i in range(2**16):
        bit = 1
        nlist = []
        removed = set()
        skipbfs = False
        for _ in range(16):
            nlist.append([])
        for j in range(16):
            if i & bit == bit and alist[j] == 0:
                # 村がなければマスを消す
                # 消したマスが他のマスの隣接リストにも含まれないように覚えておく
                removed.add(j)
            elif i & bit == bit and alist[j] == 1:
                skipbfs = True
                break
            else:
                row, col = divmod(j,4)
                if row > 0:
                    if (row-1)*4+col not in removed:
                        nlist[j].append((row-1)*4+col)
                if row < 3:
                    if (row+1)*4+col not in removed:
                        nlist[j].append((row+1)*4+col)
                if col > 0:
                    if row*4+col-1 not in removed:
                        nlist[j].append(row*4+col-1)
                if col < 3:
                    if row*4+col+1 not in removed:
                        nlist[j].append(row*4+col+1)
            bit <<= 1
        if not skipbfs and bfs(nlist, head, list(removed)) == 16:
            if not isSelfCross(removed):
                ans += 1
    return ans

def isSelfCross(removed):
    for i in list(removed):
        if i % 4 < 3 and i+5 in removed and i+1 not in removed and i+4 not in removed:
            return True
        if i % 4 > 0 and i+3 in removed and i-1 not in removed and i+4 not in removed:
            return True
    return False

def bfs(nlist, head, removed):
    visited = [False] * 16
    for u in removed:
        visited[u] = True
    queue = deque()
    queue.append(head)
    visited[head] = True
    while len(queue) > 0:
        u = queue.popleft()
        for v in nlist[u]:
            # print(f'v: {v}')
            if not visited[v]:
                queue.append(v)
                visited[v] = True
    return sum(visited)


def printans(ans):
    print(ans)

if __name__=='__main__':
    alist=readinput()
    ans=main(alist)
    printans(ans)
