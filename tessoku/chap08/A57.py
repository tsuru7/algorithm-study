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
    a=l_input()
    queries = [l_input() for _ in range(q)]
    return n,q,a,queries

def solve(n,q,a,queries):
    dbl = []
    a.insert(0,0)
    dbl.append(a)
    for i in range(1, 30):
        dbl.append([0 for _ in range(n+1)])
        for j in range(1, n+1):
            next = dbl[i-1][j]
            next = dbl[i-1][next]
            dbl[i][j] = next

    # print(*dbl, sep='\n')

    ans=[]
    for x, y in queries:
        now = x
        for i in range(30):
            if y & (1<<i) > 0:
                now = dbl[i][now]
        ans.append(now)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
