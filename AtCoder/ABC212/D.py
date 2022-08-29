import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop
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
    q=i_input()
    queries = []
    for _ in range(q):
        l=l_input()
        if l[0] == 3:
            queries.append((l[0],0))
        else:
            queries.append((l[0], l[1]))
    return q, queries

def main(q, queries):
    heap = []
    addnum = 0
    addnums = [0]*q
    ans=[]
    for i in range(q):
        p, x = queries[i]
        if p == 1:
            heappush(heap, (x-addnum, i))
            addnums[i] = addnum
        elif p == 2:
            if len(heap) > 0:
                addnum += x
            addnums[i] = addnum
        else:
            v, idx = heap[0]
            # offset = addnum - addnums[idx]
            ans.append(v+addnum)
            heappop(heap)
            if len(heap) == 0:
                addnum = 0
            addnums[i] = addnum
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    q, queries=readinput()
    ans=main(q, queries)
    printans(ans)
