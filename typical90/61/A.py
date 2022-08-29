import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

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
    q=i_input()
    queries = [l_input() for _ in range(q)]
    return q,queries

def solve(q,queries):
    ans=[]
    queue = deque()
    for t, x in queries:
        if t == 1:
            queue.appendleft(x)
        elif t == 2:
            queue.append(x)
        else:
            ans.append(queue[x-1])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    q,queries=readinput()
    ans=solve(q,queries)
    printans(ans)
