import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import deque

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
    amat = [ [0]*(i+1) + l_input() for i in range(2*n-1) ]
    return n,amat

def calc_maxhappiness(n, amat, pairs, rest_members):
    if len(pairs) == n:
        happiness = 0
        for p1, p2 in pairs:
            if p1 > p2:
                p1, p2 = p2, p1
            happiness ^= amat[p1][p2]
        return happiness

    rest_set = set(rest_members)
    p1 = rest_members[0]
    rest_set.remove(p1)
    ans = []
    for p2 in rest_members[1:]:
        pairs.append([p1, p2])
        rest_set.remove(p2)
        ans.append(calc_maxhappiness(n, amat, pairs, list(rest_set)))
        rest_set.add(p2)
        pairs.pop()
    return max(ans)

def solve(n,amat):
    members = [ i for i in range(2*n) ]
    ans = 0
    ans = calc_maxhappiness(n, amat, deque(), members)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,amat=readinput()
    ans=solve(n,amat)
    printans(ans)
