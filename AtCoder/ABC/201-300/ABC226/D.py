import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import gcd
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
    xylist = []
    for _ in range(n):
        xylist.append(l_input())
    return n,xylist

def main(n,xylist):
    katamuki = set()
    for i in range(n):
        xi, yi = xylist[i]
        for j in range(n):
            xj, yj = xylist[j]
            if i == j:
                continue
            dx = xj - xi
            dy = yj - yi
            katamuki.add((dx//gcd(dx, dy), dy//gcd(dx,dy)))

    ans=len(katamuki)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xylist=readinput()
    ans=main(n,xylist)
    printans(ans)
