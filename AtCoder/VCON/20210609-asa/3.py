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
    a=i_input()
    return a

def f(x):
    s = str(x)
    ans = 0
    for c in s:
        ans = ans*x + int(c)
    return ans

def main(a):
    # print(f(10000))
    for n in range(10, 10001):
        if f(n) == a:
            return n
        elif f(n) > a:
            return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    a=readinput()
    ans=main(a)
    printans(ans)
