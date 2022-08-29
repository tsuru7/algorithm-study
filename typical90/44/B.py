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
    head = 0
    ans=[]
    for t, x, y in queries:
        x -= 1
        y -= 1
        if t == 1:
            x = (head + x) % n
            y = (head + y) % n
            a[x], a[y] = a[y], a[x]
        elif t == 2:
            head = (head - 1) % n
        else:
            x = (head + x) % n
            ans.append(a[x])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
