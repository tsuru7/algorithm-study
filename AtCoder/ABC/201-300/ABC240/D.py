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
    a=l_input()
    return n,a

def stack_check(stack):
    v, n = stack[-1]
    while v == n:
        stack.pop()
        if len(stack) == 0:
            break
        v, n = stack[-1]
    return

def solve(n,a):
    stack = deque()
    count = 0
    ans = []
    for i in range(n):
        if len(stack) > 0 and stack[-1][0] == a[i]:
            stack[-1][1] += 1
            count += 1
            if stack[-1][0] == stack[-1][1]:
                _, n = stack.pop()
                count -= n
        else:
            stack.append([a[i], 1])
            count += 1
        ans.append(count)
        
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
