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
    n=i_input()
    points = [l_input() for _ in range(n)]
    q = i_input()
    queries = [l_input() for _ in range(q)]
    return n,points,q,queries

def solve(n,points,q,queries):
    cum = [[0 for _ in range(1501)] for _ in range(1501)]
    for x, y in points:
        cum[x][y] += 1
    for x in range(1, 1501):
        for y in range(1, 1501):
            cum[x][y] += cum[x][y-1]
    for y in range(1, 1501):
        for x in range(1, 1501):
            cum[x][y] += cum[x-1][y]
    ans=[]
    for a, b, c, d in queries:
        ans.append(cum[c][d]+cum[a-1][b-1]-cum[a-1][d]-cum[c][b-1])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,points,q,queries=readinput()
    ans=solve(n,points,q,queries)
    printans(ans)
