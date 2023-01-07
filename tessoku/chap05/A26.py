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
    q=i_input()
    queries = [i_input() for _ in range(q)]
    return q,queries

def isprime(x):
    ans = True
    i = 2
    while i*i <=x:
        if x % i == 0:
            ans = False
            break
        i += 1
    return ans

def solve(q,queries):
    ans=[]
    for x in queries:
        if isprime(x):
            ans.append('Yes')
        else:
            ans.append('No')
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    q,queries=readinput()
    ans=solve(q,queries)
    printans(ans)
