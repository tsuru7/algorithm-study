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
    r=i_input()
    return r

def main(r):
    return r*r

def printans(ans):
    print(ans)

if __name__=='__main__':
    r=readinput()
    ans=main(r)
    printans(ans)
