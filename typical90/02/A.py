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
    return n

def dfs(s, n):
    if len(s) == n:
        return [s]
    return dfs(s+'(', n) + dfs(s+')', n)

def judge(s):
    if s[0] != '(' or s[-1] != ')':
        return False
    left = s.count('(')
    right = s.count(')')
    if left != right:
        return False
    
    stack = deque()
    for c in s:
        if len(stack) == 0:
            stack.append(c)
            continue
        if stack[-1] == '(' and c == ')':
            stack.pop()
        else:
            stack.append(c)
    if len(stack) != 0:
        return False
    
    return True

def solve(n):
    all = dfs('', n)
    
    ans=[]
    for x in all:
        if judge(x):
            ans.append(x)
    ans.sort()

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
