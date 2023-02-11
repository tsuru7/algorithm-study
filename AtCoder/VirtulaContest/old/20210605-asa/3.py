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
    n=i_input()
    k=i_input()
    return n,k

def main(n,k):
    if k == 1:
        return 'YES'
    if n >= 2*k:
        return 'YES'
    else:
        return 'NO'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    printans(ans)
