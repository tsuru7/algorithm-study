import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from copy import deepcopy

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
    amat = [l_input() for _ in range(n)]
    return n,amat

def solve(n,amat):
    bmat = deepcopy(amat)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                bmat[i][j] = min(bmat[i][j], bmat[i][k]+bmat[k][j])
    # print(*amat, sep='\n')
    # print(*bmat, sep='\n')
    ans=0
    for i in range(n):
        for j in range(i+1, n):
            if bmat[i][j] < amat[i][j]:
                return -1
            for k in range(n):
                if k == i or k == j:
                    continue
                if amat[i][j] == bmat[i][k]+bmat[k][j]:
                    break
            else:
                ans += amat[i][j]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,amat=readinput()
    ans=solve(n,amat)
    printans(ans)
