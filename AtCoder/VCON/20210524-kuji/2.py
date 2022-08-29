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
    x, y, z=m_input()
    return x,y,z

def main(x,y,z):
    x -= z
    return x//(y+z)

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y,z=readinput()
    ans=main(x,y,z)
    printans(ans)
