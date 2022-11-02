import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate

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
    d = i_input()
    queries = [l_input() for _ in range(d)]
    return n,a,d,queries

def solve(n,a,d,queries):
    #  a[0]=0,    a[1],    a[2], ...,    a[x], ...,    a[n]
    # cum1[0], cum1[1], cum1[2], ..., cum1[x], ..., cum1[n]
    # 左端から x 番目までの最大値は cum1[x]
    #  b[0]=0,    b[1],    b[2], ...,    b[x], ...,    b[n]
    # cum2[0], cum2[1], cum2[2], ..., cum2[x], ..., cum2[n]
    # 右端から x 番目までの最大値は cum2[x]
    cum1 = [0 for _ in range(n+1)]
    cum2 = [0 for _ in range(n+1)]
    b = a[::-1]
    for i in range(n):
        ai = a[i]
        bi = b[i]
        cum1[i+1] = max(cum1[i], ai)
        cum2[i+1] = max(cum2[i], bi)

    ans=[]
    for l, r in queries:
        x = l-1
        max1 = cum1[x]
        x = n-r
        max2 = cum2[x]
        ans.append(max(max1, max2))
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,d,queries=readinput()
    ans=solve(n,a,d,queries)
    printans(ans)
