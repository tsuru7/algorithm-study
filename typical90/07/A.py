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
    q = i_input()
    b = [i_input() for _ in range(q)]
    return n,a,q,b

def solve(n,a,q,b):
    a.sort()
    ans=[]
    for i in range(q):
        bi = b[i]
        idx = bisect_left(a, bi)
        if idx == 0:
            ans.append(a[0]-bi)
        elif idx == n:
            ans.append(bi-a[n-1])
        else:
            ans.append(min(a[idx]-bi, bi-a[idx-1]))
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,q,b=readinput()
    ans=solve(n,a,q,b)
    printans(ans)
