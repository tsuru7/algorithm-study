import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))

INFTY = sys.maxsize
# MOD = 10**9+7
MOD = 998244353

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
    queries = []
    for _ in range(t):
        n = i_input()
        a = l_input()
        queries.append((n, a))
    return t,queries

def solve(t,queries):
    ans=[]
    for query in queries:
        n, a = query
        count = 0
        for i in range(n):
            if a[i] % 2 == 1:
                count += 1
        ans.append(count)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    t,queries=readinput()
    ans=solve(t,queries)
    printans(ans)
