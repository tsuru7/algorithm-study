import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left
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
    n,q=m_input()
    a=l_input()
    queries = []
    for _ in range(q):
        queries.append(i_input())
    return n,q,a,queries

def main(n,q,a,queries):
    a.sort()
    ans=[]
    for x in queries:
        idx = bisect_left(a, x)
        ans.append(n-idx)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=main(n,q,a,queries)
    printans(ans)
