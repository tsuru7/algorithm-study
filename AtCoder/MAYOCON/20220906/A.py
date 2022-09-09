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
    p=l_input()
    return n,p

def solve(n,p):
    count = 0
    for i in range(n):
        if p[i] != i+1:
            j = p[i]
            if j-1 < i:
                return 'NO'
            p[i], p[j-1] = p[j-1], p[i]
            count += 1
            if count > 1:
                return 'NO'
    return 'YES'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=solve(n,p)
    printans(ans)
