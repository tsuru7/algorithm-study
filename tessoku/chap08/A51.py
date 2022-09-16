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
    queries = [input().split() for _ in range(q)]
    return q, queries

def solve(q, queries):
    stack = deque()
    ans=[]
    for query in queries:
        if query[0] == '1':
            x = query[1]
            stack.append(x)
        elif query[0] == '2':
            ans.append(stack[-1])
        else:
            stack.pop()
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    q, queries=readinput()
    ans=solve(q, queries)
    printans(ans)
