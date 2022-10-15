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
    numbers = [l_input() for _ in range(n)]
    queries = [l_input() for _ in range(q)]
    return n,q,numbers,queries

def solve(n,q,numbers,queries):
    ans=[]
    for s, t in queries:
        s -= 1
        ans.append(numbers[s][t])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,numbers,queries=readinput()
    ans=solve(n,q,numbers,queries)
    printans(ans)
