import sys
sys.setrecursionlimit(10**6)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
from collections import Counter

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
    n,m=m_input()
    uvList = [l_input() for _ in range(m)]
    return n,m,uvList

def solve(n,m,uvList):
    count = [0 for _ in range(n)]
    for u, v in uvList:
        u -= 1
        v -= 1
        count[u] += 1
        count[v] += 1
    counter = Counter(count)
    if counter[1] == 2 and counter[2] == n-2:
        return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,uvList=readinput()
    ans=solve(n,m,uvList)
    printans(ans)
