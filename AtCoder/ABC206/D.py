import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from heapq import heappush, heapify, heappop
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
    a=l_input()
    return n,a

def main(n,a):
    b = a[::-1]
    nlist = []
    for _ in range(n+1):
        nlist.append(set())
    mid = (n-1)//2
    for i in range(mid+1):
        if a[i] != b[i]:
            nlist[min(a[i], b[i])].add(max(a[i], b[i]))
    # print(f'nlist: {nlist}')
    ans=0
    for i in range(1, n+1):
        nlist[i] = list(nlist[i])
        heapify(nlist[i])
        prej = 0
        while len(nlist[i]) > 0:
            j = heappop(nlist[i])
            if j != prej:
                ans += 1
                for v in nlist[j]:
                    heappush(nlist[i], v)
                nlist[j] = set()
                prej = j

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
