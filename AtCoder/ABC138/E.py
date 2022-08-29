import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict
from string import ascii_lowercase
from bisect import bisect_left, bisect_right

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
    s = input()
    t = input()
    return s, t

def solve(s, t):
    sdict = defaultdict(list)
    for idx, c in enumerate(s):
        sdict[c].append(idx)
    # print(f'sdict: {sdict}')
    i = 0
    j = 0
    count = 0
    while j < len(t):
        c = t[j]
        if len(sdict[c]) == 0:
            return -1
        idx = bisect_left(sdict[c], i)
        # print(f'i: {i}, c: {c}, idx: {idx}')
        if idx == len(sdict[c]):
            i = sdict[c][0] + 1
            count += 1
        else:
            i = sdict[c][idx] + 1
        j += 1
    return len(s)*count + i


def printans(ans):
    print(ans)

if __name__=='__main__':
    s, t=readinput()
    ans=solve(s, t)
    printans(ans)
