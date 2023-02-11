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
    a=l_input()
    return n,a

def solve(n,a):
    b = [0]*4
    ans=0
    for i in range(n):
        b[0] = 1
        ai = a[i]
        for j in range(ai):
            if b[3] == 1:
                ans += 1
            b[3] = b[2]
            b[2] = b[1]
            b[1] = b[0]
            b[0] = 0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
