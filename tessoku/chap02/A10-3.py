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
    d = i_input()
    queries = [l_input() for _ in range(d)]
    return n,a,d,queries

def solve(n,a,d,queries):
    cum1 = [0 for _ in range(n)]
    cum2 = [0 for _ in range(n)]
    cum1[0] = a[0]
    for i in range(1, n):
        cum1[i] = max(cum1[i-1], a[i])
    cum2[n-1] = a[n-1]
    for i in range(n-1)[::-1]:
        cum2[i] = max(cum2[i+1], a[i])
    ans=[]
    for l, r in queries:
        l -= 1
        r -= 1
        max1 = cum1[l-1]
        max2 = cum2[r+1]
        ans.append(max(max1, max2))
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,d,queries=readinput()
    ans=solve(n,a,d,queries)
    printans(ans)
