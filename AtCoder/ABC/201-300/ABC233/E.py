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
    x = input()
    return x

def main(x):
    n = len(x)
    cumsum = [0]*n
    for i in range(n):
        num = int(x[i])
        if i == 0:
            cumsum[i] = num
        else:
            cumsum[i] = cumsum[i-1]+num
    stack = deque()
    carry = 0
    for i in range(n)[::-1]:
        temp = cumsum[i] + carry
        carry = temp // 10
        digit = temp % 10
        stack.appendleft(str(digit))
    if carry > 0:
        stack.appendleft(str(carry))
    ans = ''.join(stack)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    printans(ans)
