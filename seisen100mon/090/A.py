from cmath import sqrt
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
    n,m=m_input()
    circle1 = [l_input() for _ in range(n)]
    circle2 = [l_input() for _ in range(m)]
    return n,m,circle1,circle2

def solve(n,m,circle1,circle2):
    if m == 0:
        circle1.sort(key=lambda x: x[2])
        return circle1[0][2]
        
    r = [INFTY for _ in range(m)]
    for i in range(m):
        xi, yi = circle2[i]
        ri = r[i]
        for j in range(n):
            xj, yj, rj = circle1[j]
            dij = sqrt((xi-xj)**2+(yi-yj)**2)
            ri = min(ri, dij - rj)
        r[i] = ri
    
    for i in range(m):
        xi, yi = circle2[i]
        for j in range(i+1, m):
            xj, yj = circle2[j]
            dij = sqrt((xi-xj)**2+(yi-yj)**2)
            r[i] = min(r[i], dij/2)
            r[j] = min(r[j], dij/2)

    return min(r)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,circle1,circle2=readinput()
    ans=solve(n,m,circle1,circle2)
    printans(ans)
