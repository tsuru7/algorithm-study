import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right
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
    s = input()
    w = l_input()
    return n,s,w

def solve(n,s,w):
    adult = []
    child = []
    for c, wi in zip(s, w):
        if c == '0':
            child.append(wi)
        else:
            adult.append(wi)
    adult.sort()
    child.sort()
    n_adult = len(adult)
    n_child = len(child)

    adult = deque(adult)
    child = deque(child)

    w.sort()
    w.insert(0, 0)
    w.append(10**9+1)
    point = 0
    for wi in w:
        while len(adult) > 0 and adult[0] < wi:
            adult.popleft()
        while len(child) > 0 and child[0] < wi:
            child.popleft()
        point = max(point, len(adult) + n_child - len(child))


    return point

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s,w=readinput()
    ans=solve(n,s,w)
    printans(ans)
