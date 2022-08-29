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
    x=i_input()
    return x

def main(x):
    ans = (x // 500) * 1000
    x = x % 500
    ans += (x // 5) * 5
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    printans(ans)
