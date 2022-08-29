import sys
sys.setrecursionlimit(10**6)
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
    n=i_input()
    xy = []
    for _ in range(n):
        xy.append(l_input())
    return n,xy

def main(n,xy):
    ans=0
    for i in range(n-2):
        xi, yi = xy[i]
        for j in range(i+1, n-1):
            xj, yj = xy[j]
            for k in range(j+1, n):
                xk, yk = xy[k]
                a = xj - xi
                b = yj - yi
                c = xk - xi
                d = yk - yi
                det = abs(a*d - b*c)
                if det != 0:
                    ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xy=readinput()
    ans=main(n,xy)
    printans(ans)
