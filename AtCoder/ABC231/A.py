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
    d=i_input()
    return d

def main(d):
    ans=d/100
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    d=readinput()
    ans=main(d)
    printans(ans)
