import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
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
    n,d=m_input()
    jobs = [l_input() for _ in range(n)]
    return n,d,jobs

def solve(n,d,jobs):
    heap = []
    jobs.sort(key=lambda x: x[0])
    j = 0
    ans=0
    for i in range(1, d+1):
        while j < n and jobs[j][0] <= i:
            heappush(heap, -jobs[j][1])
            j += 1
        if len(heap) > 0:
            ans -= heappop(heap)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d,jobs=readinput()
    ans=solve(n,d,jobs)
    printans(ans)
