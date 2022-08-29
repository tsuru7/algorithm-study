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
    n=i_input()
    s = l_input()
    t = l_input()
    return n,s,t

def main(n,s,t):
    heap = []
    for i in range(n):
        heappush(heap, (t[i], i))
    mint = [INFTY]*n
    count = 0
    while count < n:
        # print(heap)
        # print(mint)
        ti, i = heappop(heap)
        if mint[i] == INFTY:
            count += 1
            mint[i] = ti
            j = i + 1
            if j == n:
                j = 0
            heappush(heap, (ti+s[i], j))
        else:
            if ti < mint[i]:
                mint[i] = ti
                j = i + 1
                if j == n:
                    j = 0
                heappush(heap, (ti+s[i], j))

    return mint

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,s,t=readinput()
    ans=main(n,s,t)
    printans(ans)
