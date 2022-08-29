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
    d,n=m_input()
    return d,n

def main(d,n):
    if n == 100:
        n = 101
    ans=n*100**d
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    d,n=readinput()
    ans=main(d,n)
    printans(ans)
