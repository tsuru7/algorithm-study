import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import combinations

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
    return n,k

def solve(n,k):
    if k > (n-1)*(n-2)//2:
        return [-1]
    nedges = n-1 + (n-1)*(n-2)//2 - k
    ans = []
    ans.append(nedges)
    for i in range(n-1):
        ans.append((i+1, n))
    nedges -= n-1
    if nedges > 0:
        for pair in combinations(range(1, n), 2):
            ans.append(pair)
            nedges -= 1
            if nedges == 0:
                break
    return ans

def printans(ans):
    print(ans[0])
    if ans[0] > 0:
        for u, v in ans[1:]:
            if u > v:
                u, v = v, u
            print(u, v)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
