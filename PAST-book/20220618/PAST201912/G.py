import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import combinations

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
    amat = [ [0]*n for _ in range(n) ]
    for i in range(n-1):
        l = l_input()
        for k, v in enumerate(l):
            j = i+k+1
            amat[i][j] = v
            amat[j][i] = v
    return n,amat

def solve(n,amat):
    # print(*amat, sep='\n')

    ans=-INFTY
    for x in range(2**n):
        group0 = set()
        for b in range(n):
            bit = 1<<b
            if x & bit == bit:
                group0.add(b)
        group1 = set(range(n)) - group0
        happy = 0
        for i, j in combinations(group0, 2):
            happy += amat[i][j]
        for i, j in combinations(group1, 2):
            happy += amat[i][j]
        # if happy >= ans:
        #     print(f'group0: {group0}, group1: {group1}, happy: {happy}')
        ans = max(ans, happy)
    
    for x in range(3**n):
        group0 = set()
        group1 = set()
        for b in range(n):
            bit0 = 3**b
            # bit1 = 3**b+1
            if (x // bit0) % 3 == 1:
                group0.add(b)
            elif (x // bit0) % 3 == 2:
                group1.add(b)
        group2 = set(range(n)) - group0 - group1
        # print(len(group0), len(group1), len(group2))
        happy = 0
        for i, j in combinations(group0, 2):
            happy += amat[i][j]
        for i, j in combinations(group1, 2):
            happy += amat[i][j]
        for i, j in combinations(group2, 2):
            happy += amat[i][j]
        # if happy > ans:
        #     print(f'group0: {group0}, group1: {group1}, group2: {group2}, happy: {happy}')
        ans = max(ans, happy)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,amat=readinput()
    ans=solve(n,amat)
    printans(ans)
