from collections import deque
import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
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
    b = deque()
    for i in range(n):
        if i % 2 == 0:
            b.append(a[i])
        else:
            b.appendleft(a[i])
    if n % 2 == 0:
        return list(b)
    else:
        return list(b)[::-1]

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
