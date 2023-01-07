import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    queries = [l_input() for _ in range(q)]
    return n,queries

def solve(n,queries):
    graph = dict()
    ans=[]
    for t, a, b in queries:
        if t == 1:
            if a not in graph:
                graph[a] = {b}
            else:
                graph[a].add(b)
        elif t == 2:
            if a in graph:
                graph[a].discard(b)
        elif t == 3:
            if a not in graph or b not in graph:
                ans.append('No')
            else:
                if b in graph[a] and a in graph[b]:
                    ans.append('Yes')
                else:
                    ans.append('No')

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,queries=readinput()
    ans=solve(n,queries)
    printans(ans)
