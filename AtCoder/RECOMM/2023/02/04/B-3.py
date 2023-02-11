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
    s1 = input()
    s2 = input()
    s3 = input()
    return s1, s2, s3

def solve(s1, s2, s3):
    # s1 = [ord(c) for c in s1]
    # s2 = [ord(c) for c in s2]
    # s3 = [ord(c) for c in s3]
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    chars = list(set(s1+s2+s3))
    if len(chars) > 10:
        return 'UNSOLVABLE'
    for p in permutations(range(10), len(chars)):
        xtbl = dict()
        for i, d in enumerate(p):
            xtbl[chars[i]] = d
        # print(xtbl)
        # print(f's1: {s1}, s2: {s2}, s3: {s3}')
        if xtbl[s1[0]] == 0 or xtbl[s2[0]] == 0 or xtbl[s3[0]] == 0:
            continue
        n1 = 0
        n2 = 0
        n3 = 0
        for c in s1:
            n1 *= 10
            n1 += xtbl[c]
        for c in s2:
            n2 *= 10
            n2 += xtbl[c]
        for c in s3:
            n3 *= 10
            n3 += xtbl[c]
        # print(f'n1: {n1}, n2: {n2}, n3: {n3}')
        if n1 + n2 == n3:
            return (n1, n2, n3)
    return 'UNSOLVABLE'

def printans(ans):
    if type(ans) == tuple:
        print(*ans, sep='\n')
    else:
        print(ans)

if __name__=='__main__':
    s1, s2, s3=readinput()
    ans=solve(s1, s2, s3)
    printans(ans)
