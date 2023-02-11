import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
# from collections import deque

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
    n,m=m_input()
    a=l_input()
    c=l_input()
    return n,m,a,c

def solve(n,m,a,c):
    b = [0]*(m+1)
    for i in range(m+1)[::-1]:
        x = c[i+n]
        for j in range(1, m-i+1):
            # print(f'i, j: {(i, j)}')
            if n-j < 0:
                break
            x -= a[n-j]*b[i+j]
        x //= a[n]
        b[i] = x
    return b

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,m,a,c=readinput()
    ans=solve(n,m,a,c)
    printans(ans)
