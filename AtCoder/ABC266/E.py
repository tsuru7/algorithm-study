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
    # p6 = 1 - (5/6)**n
    # p5 = (4/6)**(n-1)*(1/6)
    # p4 = (3/6)**(n-1)*(1/6)
    # p3 = (2/6)**(n-1)*(1/6)
    # p2 = (1/6)**(n-1)*(1/6)
    # p1 = (1/6)**(n-1)*(1/6)
    # p = p1+p2+p3+p4+p5+p6
    # prob = (p1*1+p2*2+p3*3+p4*4+p5*5+p6*6)/p
    prob = (1.0-(1/2)**(n))*5 + (1/2)**(n)*2
    return prob

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
