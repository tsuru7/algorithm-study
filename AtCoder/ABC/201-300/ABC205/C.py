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
        return '='
    if c % 2 == 0:
        if abs(a) < abs(b):
            return '<'
        elif abs(a) > abs(b):
            return '>'
        else:
            return '='
    else:
        if a < b:
            return '<'
        elif a > b:
            return '>'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c=readinput()
    ans=main(a,b,c)
    printans(ans)
