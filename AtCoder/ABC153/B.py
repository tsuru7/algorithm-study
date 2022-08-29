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
    h,n=m_input()
    a=l_input()
    return h,n,a

def main(h,n,a):
    if sum(a) >= h:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,n,a=readinput()
    ans=main(h,n,a)
    printans(ans)
