import sys
sys.setrecursionlimit(10**5)
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
    n=i_input()
    ab = []
    for _ in range(n):
        ab.append(l_input())
    return n,ab

def main(n,ab):
    ab.sort()
    heap = []

    point = 0
    ans = []
    j = 0
    a, b = ab[j]
    for i in range(1, n+1):
        while a == i:
            heappush(heap, -b)
            j += 1
            if j == n:
                break
            a, b = ab[j]
        point += -heappop(heap)
        ans.append(point)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    printans(ans)
