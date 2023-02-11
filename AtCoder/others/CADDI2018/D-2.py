import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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
    a = [i_input() for _ in range(n)]
    return n,a

def solve(n,a):
    even = 0
    odd = 0
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        return 'second'
    else:
        return 'first'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
