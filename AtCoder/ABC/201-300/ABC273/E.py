import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict

class Node:
    def __init__(self, x, p):
        self.data = x
        self.parent = p
        self.children = []
    
    def add(self, child):
        self.children.append(child)

    def getData(self):
        return self.data

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
    return q,queries

def solve(q,queries):
    ans=[]
    root = Node(-1, -1)
    now = root
    pages = dict()
    for query in queries:
        if query[0] == 'ADD':
            x = int(query[1])
            child = Node(x, now)
            # now.add(child)
            now = child
            ans.append(x)
        elif query[0] == 'DELETE':
            # print(f'DELETE a: {a}')
            if now == root:
                x = -1
            else:
                now = now.parent
                x = now.getData()
            ans.append(x)
        elif query[0] == 'SAVE':
            y = int(query[1])
            pages[y] = now
            x = now.getData()
            ans.append(x)
        else:
            z = int(query[1])
            if z not in pages:
                now = root
            else:
                now = pages[z]
            x = now.getData()
            ans.append(x)
        # print(f'a: {a}, pages: {pages}, ans: {ans}')
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    q,queries=readinput()
    ans=solve(q,queries)
    printans(ans)
