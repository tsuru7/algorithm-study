import sys
INFTY = sys.maxsize
from collections import deque

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    stack = deque()
    minvalue = INFTY
    for x in range(2**(n-1)):
        # print(bin(x))
        bit = 1
        stack.append(a[0])
        # print(stack)
        for i in range(1, n):
            if x & bit == bit:
                stack.append(a[i])
            else:
                tmp = stack.pop()
                stack.append(tmp | a[i])
            bit = bit * 2
            # print(stack)
        val = stack.pop()
        while len(stack) > 0:
            val = val ^ stack.pop()
        # print(val)
        minvalue = min(minvalue, val)
    return minvalue

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
