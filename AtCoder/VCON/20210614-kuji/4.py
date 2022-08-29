import sys
sys.setrecursionlimit(10**5)
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

def main(n,s):
    queue = deque()
    for c in s:
        if c == ')':
            if len(queue) > 0 and queue[-1] == '(':
                queue.pop()
            else:
                queue.append(c)
        else:
            queue.append(c)
    nrp = queue.count(')')
    nlp = queue.count('(')

    ans='('*nrp + s + ')'*nlp
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    printans(ans)
