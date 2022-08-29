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
    n,q=m_input()
    a=l_input()
    queries = [ i_input() for _ in range(q) ]
    return n,q,a,queries

def solve(n,q,a,queries):
    a.sort()
    cumsum = [0]*n
    cumsum[0] = a[0]
    for i in range(1, n):
        cumsum[i] = cumsum[i-1] + a[i]
    ans=[]
    for x in queries:
        tmp = 0
        if x <= a[0]:
            tmp = cumsum[n-1] - n*x
        elif x >= a[n-1]:
            tmp = n*x - cumsum[n-1]
        else:
            l = bisect_left(a, x)
            tmp = x*l - cumsum[l-1]
            tmp += cumsum[n-1] - cumsum[l-1] - x*(n-l)
        ans.append(tmp)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
