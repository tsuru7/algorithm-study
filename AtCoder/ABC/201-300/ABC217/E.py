import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque
from heapq import heappush, heappop
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
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    return q, queries

def main(q, queries):
    a = []
    top = 0
    ans=[]
    # print(f'queries: {queries}')
    stock = deque()
    for query in queries:
        # print(f'query: {query}')
        if query[0] == 1:
            stock.append(query[1])
#            a.append(query[1])
        elif query[0] == 2:
            if len(a) > 0:
                tmp = heappop(a)
            else:
                tmp = stock.popleft()
            ans.append(tmp)
        else:
            for i in range(len(stock)):
                heappush(a, stock[i])
            stock = deque()
            
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    q, queries=readinput()
    ans=main(q, queries)
    printans(ans)
