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
    return n,d

def main(n,d):
    if n == 100:
        n = 101    
    return n*100**d

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d=readinput()
    ans=main(n,d)
    printans(ans)
