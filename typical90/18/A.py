import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import pi, cos, sin, sqrt, atan

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
    t=i_input()
    l,x,y=m_input()
    q = i_input()
    eList = [i_input() for _ in range(q)]
    return t,l,x,y,q,eList

def solve(t,l,x,y,q,eList):
    r = l/2
    omega = 2*pi/t
    ans=[]
    for e in eList:
        theta = omega*e
        xi = 0
        yi = -r*sin(theta)
        zi = r-r*cos(theta)
        dist = sqrt((x-xi)**2 + (y-yi)**2)
        hight = zi
        ans.append(atan(hight/dist)*180/pi)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    t,l,x,y,q,eList=readinput()
    ans=solve(t,l,x,y,q,eList)
    printans(ans)
