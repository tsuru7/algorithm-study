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
    l1,r1,l2,r2=m_input()
    return l1,r1,l2,r2

def solve(l1,r1,l2,r2):
    count = 0
    for x in range(101):
        if l1 <= x <= r1 and l2 <= x <= r2:
            count += 1
    return max(0, count-1)

def printans(ans):
    print(ans)

if __name__=='__main__':
    l1,r1,l2,r2=readinput()
    ans=solve(l1,r1,l2,r2)
    printans(ans)
