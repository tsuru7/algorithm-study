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
    x,a,b=m_input()
    return x,a,b

def main(x,a,b):
    if b <= a:
        return 'delicious'
    elif b <= a + x:
        return 'safe'
    else:
        return 'dangerous'

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,a,b=readinput()
    ans=main(x,a,b)
    printans(ans)
