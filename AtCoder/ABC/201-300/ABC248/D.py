import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    q=i_input()
    queries = [ l_input() for _ in range(q) ]
    return n,a,q,queries

def solve(n,a,q,queries):
    countLists = [ [] for _ in range(n) ]
    for i in range(n):
        countLists[a[i]-1].append(i)
    ans=[]
    for l, r, x in queries:
        l -= 1
        r -= 1
        x -= 1
        count_l = bisect_left(countLists[x], l)
        count_r = bisect_right(countLists[x], r)
        ans.append(count_r - count_l )
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,q,queries=readinput()
    ans=solve(n,a,q,queries)
    printans(ans)
