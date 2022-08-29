import sys
sys.setrecursionlimit(10**5)
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
    r,x,y=m_input()
    return r,x,y

def main(r,x,y):
    d2 = x**2 + y**2
    if d2 < r**2:
        return 2
    step = 1
    dist = r*step
    while dist**2 < d2:
        step += 1
        dist = r*step
    return step

def printans(ans):
    print(ans)

if __name__=='__main__':
    r,x,y=readinput()
    ans=main(r,x,y)
    printans(ans)
