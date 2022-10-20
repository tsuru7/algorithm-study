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
    n,m=m_input()
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = m_input()
        graph[a].append(b)
        graph[b].append(a)
    return n,m,graph

def solve(n,m,graph):
    ans=[]
    for i in range(1, n+1):
        ans.append(graph[i])
    return ans

def printans(ans):
    for i in range(n):
        print(f'{i+1}: {{', end='')
        ansi = ans[i]
        for i in range(len(ansi)-1):
            print(f'{ansi[i]}, ', end='')
        if len(ansi) > 0:
            print(f'{ansi[-1]}', end='')
        print(f'}}')


if __name__=='__main__':
    n,m,graph=readinput()
    ans=solve(n,m,graph)
    printans(ans)
