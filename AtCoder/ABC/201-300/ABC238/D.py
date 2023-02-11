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
    t=i_input()
    queries = [ l_input() for _ in range(t) ]
    return t,queries

def solve(t,queries):    
    ans=[]
    for a, s in queries:
        u = s - 2*a
        if u < 0:
            ans.append('No')
        elif a & u == 0:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    t,queries=readinput()
    ans=solve(t,queries)
    printans(ans)
