import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations

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
    rclist = [ l_input() for _ in range(n) ]
    return n,rclist

def isValid1(row, rclist):
    for r, c in rclist:
        if r != row[c]:
            return False
    return True

def isValid2(row):
    rcp = set()
    rcm = set()
    for c, r in enumerate(row):
        if r+c in rcp:
            return False
        else:
            rcp.add(r+c)
        if r-c in rcm:
            return False
        else:
            rcm.add(r-c)
    return True

def makeMat(row):
    mat = [ ['.']*8 for _ in range(8) ]
    for c, r in enumerate(row):
        mat[r][c] = 'Q'
    for r in range(8):
        mat[r] = ''.join(mat[r])
    return mat

def solve(n,rclist):
    for row in permutations(range(8)):
        if not isValid1(row, rclist):
            continue
        if isValid2(row):
            return makeMat(row)

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,rclist=readinput()
    ans=solve(n,rclist)
    printans(ans)
