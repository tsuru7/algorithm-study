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
    x = input()
    return x

def main(x):
    if x.find('.') == -1:
        return x
    return x[:x.find('.')]

def printans(ans):
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    printans(ans)
