import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from math import pi
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
    r = []
    for _ in range(n):
        r.append(i_input())
    return n,r

def main(n,r):
    r.sort(reverse=True)
    ans=0
    flag = 1
    for i in range(len(r)):
        ans += flag * r[i]*r[i]
        flag *= -1
    ans *= pi
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,r=readinput()
    ans=main(n,r)
    printans(ans)
