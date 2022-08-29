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
    s = input()
    return n,s

def solve(n,s):
    l = deque()
    r = deque()
    l.append(0)
    flag_l = True
    for i in range(len(s)):
        c = s[i]
        if c == 'L':
            if flag_l:
                r.appendleft(l.pop())
            l.append(i+1)
            flag_l = True
        else:
            if not flag_l:
                l.append(r.popleft())
            r.appendleft(i+1)
            flag_l = False
        # print(f'c: {c}, l: {l}, r: {r}')
    ans = list(l)+list(r)
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,s=readinput()
    ans=solve(n,s)
    printans(ans)
