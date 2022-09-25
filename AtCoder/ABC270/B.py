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
    x,y,z=m_input()
    return x,y,z

def solve(x,y,z):
    if x < 0:
        x *= -1
        y *= -1
        z *= -1
    if y > x or y < 0:
        return x
    if z > y:
        return -1
    if z < 0:
        return -2*z + x
    if z > 0:
        return x

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y,z=readinput()
    ans=solve(x,y,z)
    printans(ans)
