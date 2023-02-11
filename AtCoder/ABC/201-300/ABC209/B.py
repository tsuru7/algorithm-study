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
    n,x=m_input()
    a=l_input()
    return n,x,a

def main(n,x,a):
    for i in range(n):
        if i % 2 == 1:
            a[i] -= 1
    goukei = sum(a)
    if goukei > x:
        return 'No'
    else:
        return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,a=readinput()
    ans=main(n,x,a)
    printans(ans)
