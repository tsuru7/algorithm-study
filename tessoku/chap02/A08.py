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
    h,w=m_input()
    xmap = [l_input() for _ in range(h)]
    q = i_input()
    queries = [l_input() for _ in range(q)]
    return h,w,xmap,q,queries

def solve(h,w,xmap,q,queries):
    cum = [[0 for _ in range(w+1)] for _ in range(h+1)]
    for row in range(1, h+1):
        for col in range(1, w+1):
            cum[row][col] = cum[row][col-1] + xmap[row-1][col-1]
    for col in range(1, w+1):
        for row in range(1, h+1):
            cum[row][col] += cum[row-1][col]
    ans=[]
    for a, b, c, d in queries:
        tmp = cum[c][d] - cum[c][b-1] - cum[a-1][d] + cum[a-1][b-1]
        ans.append(tmp)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    h,w,xmap,q,queries=readinput()
    ans=solve(h,w,xmap,q,queries)
    printans(ans)
