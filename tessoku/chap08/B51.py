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
    s = input()
    return s

def solve(s):
    stack = deque()
    ans=[]
    for i in range(len(s)):
        if len(stack) > 0 and stack[-1][0] == '(' and s[i] == ')':
            ans.append((stack[-1][1], i+1))
            stack.pop()
        else:
            stack.append((s[i], i+1))

    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
