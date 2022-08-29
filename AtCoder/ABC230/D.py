import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappop, heappush
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
    n,d=m_input()
    lr = []
    for _ in range(n):
        lr.append(l_input())
    return n,d,lr

def tidyup(heapq, destroySet):
    if len(heapq) == 0:
        return heapq
    _ , idx = heapq[0]
    while idx in destroySet:
        heappop(heapq)
        if len(heapq) == 0:
            return heapq
        _, idx = heapq[0]
    return heapq

def destroy(heapq, tail, destroySet):
    if len(heapq) == 0:
        return heapq, destroySet
    top, _ = heapq[0]
    while top <= tail:
        _, idx = heappop(heapq)
        destroySet.add(idx)
        if len(heapq) == 0:
            return heapq, destroySet
        top, _ = heapq[0]
    return heapq, destroySet

def main(n,d,lr):
    l_heap = []
    r_heap = []
    for i, (l, r) in enumerate(lr):
        heappush(l_heap, (l, i))
        heappush(r_heap, (r, i))
    destroySet = set()
    punch = 0

    # print(f'l_heap: {l_heap}, r_heap: {r_heap}, destroySet: {destroySet}')
    while len(r_heap) > 0:
        head, idx = heappop(r_heap)
        tail = head+d-1
        destroySet.add(idx)
        punch += 1

        r_heap, destroySet = destroy(r_heap, tail, destroySet)
        l_heap, destroySet = destroy(l_heap, tail, destroySet)

        tidyup(r_heap, destroySet)
        # print(f'l_heap: {l_heap}, r_heap: {r_heap}, destroySet: {destroySet}')

    return punch

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d,lr=readinput()
    ans=main(n,d,lr)
    printans(ans)
