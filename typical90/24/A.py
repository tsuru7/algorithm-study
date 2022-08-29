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
    n,k=m_input()
    a=l_input()
    b=l_input()
    return n,k,a,b

def solve(n,k,a,b):
    tmp = 0
    for i in range(n):
        tmp += abs(a[i]-b[i])
    if tmp > k:
        return 'No'
    else:
        if (k-tmp) % 2 == 0:
            return 'Yes'
        else:
            return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a,b=readinput()
    ans=solve(n,k,a,b)
    printans(ans)
