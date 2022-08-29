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

def main(n):
    ans=deque()
    while n > 0:
        if n % 2 == 1:
            n -= 1
            ans.appendleft('A')
        else:
            n //= 2
            ans.appendleft('B')
    ans = ''.join(ans)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
