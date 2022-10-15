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
    amat = [input() for _ in range(n)]
    return n,amat

def solve(n,amat):
    for i in range(n):
        for j in range(i):
            if amat[i][j] == 'W' and amat[j][i] != 'L':
                return 'incorrect'
            if amat[i][j] == 'L' and amat[j][i] != 'W':
                return 'incorrect'
            if amat[i][j] == 'D' and amat[j][i] != 'D':
                return 'incorrect'

    return 'correct'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,amat=readinput()
    ans=solve(n,amat)
    printans(ans)
