import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappop, heappush, heapify

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
    n,k=m_input()
    p=l_input()
    return n,k,p

def solve(n,k,p):
    heap = p[:k]
    heap.sort(reverse=True)
    heapify(heap)
    rest = []
    ans=[]
    ans.append(heap[0])
    for i in range(k, n):
        pi = p[i]
        if pi > heap[0]:
            rest.append(heappop(heap))
            heappush(heap, pi)
        else:
            rest.append(pi)
        ans.append(heap[0])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,k,p=readinput()
    ans=solve(n,k,p)
    printans(ans)
