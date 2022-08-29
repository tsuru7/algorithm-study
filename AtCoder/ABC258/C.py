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
    s = input()
    queries = [l_input() for _ in range(q)]
    return n,q,s,queries

def solve(n,q,s,queries):
    ans = []
    head = 0
    tail = n-1
    for i, x in queries:
        if i == 1:
            head -= x
            if head < 0:
                head += n
            tail -= x
            if tail < 0:
                tail += n
        else:
            target = (head + x - 1) % n
            ans.append(s[target])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,s,queries=readinput()
    ans=solve(n,q,s,queries)
    printans(ans)
