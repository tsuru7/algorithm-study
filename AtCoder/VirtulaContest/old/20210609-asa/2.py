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
    a = input()
    b = input()
    return a,b

def main(a,b):
    if len(a) == len(b):
        if a > b:
            return "GREATER"
        elif a < b:
            return 'LESS'
        else:
            return 'EQUAL'
    else:
        if len(a) > len(b):
            return 'GREATER'
        elif len(a) < len(b):
            return 'LESS'


def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    printans(ans)
