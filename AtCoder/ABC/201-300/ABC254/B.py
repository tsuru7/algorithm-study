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
    return n

def solve(n):
    a = []
    for i in range(n):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(a[i-1][j-1]+a[i-1][j])
        a.append(tmp)
            
    return a

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
