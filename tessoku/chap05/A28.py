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
    queries = [input().split() for _ in range(n)]
    return n,queries

def solve(n,queries):
    MOD = 10000
    ans=[]
    x = 0
    for query in queries:
        ti = query[0]
        ai = int(query[1])
        if ti == '+':
            x += ai
            x %= MOD
        elif ti == '-':
            x -= ai
            x %= MOD
        elif ti == '*':
            x *= ai
            x %= MOD
        ans.append(x)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,queries=readinput()
    ans=solve(n,queries)
    printans(ans)
