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
    a=l_input()
    q = i_input()
    queries = [l_input() for _ in range(q)]
    return n,a,queries

def solve(n,a,queries):
    changed = dict()
    for i in range(n):
        changed[i+1] = a[i]
    base = 0
    ans=[]
    for query in queries:
        if query[0] == 1:
            x = query[1]
            base = x
            changed.clear()
        elif query[0] == 2:
            i = query[1]
            x = query[2]
            if i in changed:
                changed[i] += x
            else:
                changed[i] = x
        else:
            i = query[1]
            if i in changed:
                ans.append(changed[i] + base)
            else:
                ans.append(base)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,queries=readinput()
    ans=solve(n,a,queries)
    printans(ans)
