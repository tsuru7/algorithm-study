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
    dist_b = [0]*101
    j = 0
    ans = []
    point = 0
    for i in range(n):
        a, b = ab[j]
        while a-1 == i:
            dist_b[b] += 1
            if j == n-1:
                break
            j += 1
            a, b = ab[j]
        printd(f'i: {i}, dist_b: {dist_b}')
        for v in range(100, 0, -1):
            if dist_b[v] > 0:
                break
        point += v
        ans.append(point)
        dist_b[v] -= 1

    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    printans(ans)
