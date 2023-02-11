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
    a,b,c=m_input()
    return a,b,c

def main(a,b,c):
    if a == b:
        return c
    elif b == c:
        return a
    elif c == a:
        return b
    else:
        return 0

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c=readinput()
    ans=main(a,b,c)
    printans(ans)
