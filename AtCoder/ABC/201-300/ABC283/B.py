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
    return n,a,q,queries

def solve(n,a,q,queries):
    ans=[]
    for query in queries:
        if query[0] == 1:
            k, x = query[1:]
            k -= 1
            a[k] = x
        else:
            k = query[1]
            k -= 1
            ans.append(a[k])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,q,queries=readinput()
    ans=solve(n,a,q,queries)
    printans(ans)
