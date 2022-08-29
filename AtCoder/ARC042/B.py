import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from math import sqrt
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
    x, y = m_input()
    n=i_input()
    xy = []
    for _ in range(n):
        xy.append(l_input())
    return n,x,y,xy

def distance(x0, y0, x1, y1, x2, y2):
    if x1 == x2:
        return abs(x1 - x0)
    a = (y2 - y1)/(x2 - x1)
    d = abs(a*x0 - y0 - a*x1 + y1)/sqrt(a**2+1)
    return d

def main(n,x,y,xy):
    x0 = x
    y0 = y
    ans=INFTY
    for i, tmp in enumerate(xy):
        x2, y2 = tmp
        if i == 0:
            x1 = x2
            y1 = y2
            continue
        d = distance(x0, y0, x1, y1, x2, y2)
        ans = min(ans, d)
        x1 = x2
        y1 = y2
    else:
        x2, y2 = xy[0]
        d = distance(x0, y0, x1, y1, x2, y2)
        ans = min(ans, d)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,xy=readinput()
    ans=main(n,x,y,xy)
    printans(ans)
