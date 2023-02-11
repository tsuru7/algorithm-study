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
    l=l_input()
    return l

def main(l):
    ans=sum(l)-max(l)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    l=readinput()
    ans=main(l)
    printans(ans)
