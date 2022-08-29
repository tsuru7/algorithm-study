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
    n,q=m_input()
    queries = []
    for _ in range(q):
        queries.append(l_input())
    return n,q,queries

def main(n,q,queries):
    ans=[]
    train = [ [-1, -1] for _ in range(n+1)]
    for query in queries:
        if query[0] == 1:
            tail = query[1]
            head = query[2]
            train[tail][1] = head
            train[head][0] = tail
        elif query[0] == 2:
            tail = query[1]
            head = query[2]
            train[tail][1] = -1
            train[head][0] = -1
        elif query[0] == 3:
            t = query[1]
            ans.append(subtrain(t, train))
    return ans

def subtrain(t, train):
    ans = deque()
    ans.append(t)
    s = t
    while train[s][0] != -1:
        s = train[s][0]
        ans.appendleft(s)
    s = t
    while train[s][1] != -1:
        s = train[s][1]
        ans.append(s)
    return len(ans), list(ans)


def printans(ans):
    for n, l in ans:
        print(n, ' '.join(map(str, l)))

if __name__=='__main__':
    n,q,queries=readinput()
    ans=main(n,q,queries)
    printans(ans)
