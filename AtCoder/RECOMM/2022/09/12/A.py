# https://atcoder.jp/contests/tenka1-2018/tasks/tenka1_2018_c

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
    a = [i_input() for _ in range(n)]
    return n,a

def solve(n,a):
    '''
    1,2,3,6,8
    8,6,3,2,1
    8,1,2,3,6
    |a0 - a1| + |a1 - a2| + |a2 - a3| + |a3 - a4|
    a0 > a1のとき
    a0 - a1 - a1 + a2 + a2 - a3 - a3 + a4
    a0 - 2*a1 + 2*a2 - 2*a3 + a4
    2  - 2*8  + 2*1  - 2*6  + 3
    '''

    if n == 2:
        return abs(a[0]-a[1])
    if n == 3:
        a.sort()
        return max(abs(a[0]-a[2]) + abs(a[2]-a[1]), abs(a[2]-a[0]) + abs(a[0]-a[1]))

    a.sort(reverse=True)
    aa = deque(a)
    b = []
    flag = True
    while len(aa) > 2:
        if flag:
            b.append(aa.popleft())
        else:
            b.append(aa.pop())
        flag = not flag
    d = [aa[0]] + b + [aa[-1]]
    c = [aa[-1]] + b + [aa[0]]
    ans1=0
    for i in range(n-1):
        ans1 += abs(d[i+1]-d[i])
    ans2 = 0
    for i in range(n-1):
        ans2 += abs(c[i+1]-c[i])
    return max(ans1, ans2)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
