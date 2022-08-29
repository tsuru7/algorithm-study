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
    queries = [ l_input() for _ in range(q) ]
    return q,queries

def solve(q,queries):
    queue = deque()
    ans=[]
    for query in queries:
        if query[0] == 1:
            x = query[1]
            c = query[2]
            queue.append([x, c])
        elif query[0] == 2:
            sum = 0
            c = query[1]
            y, d = queue.popleft()
            while d < c:
                sum += y*d
                c -= d
                y, d = queue.popleft()
            if d > c:
                sum += y*c
                d -= c
                queue.appendleft([y, d])
            else:
                sum += y*c
            ans.append(sum)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    q,queries=readinput()
    ans=solve(q,queries)
    printans(ans)
