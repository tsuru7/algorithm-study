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
    ans=[]
    for i in range(n):
        if a[i] != x:
            ans.append(a[i])
    return ans

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    n,x,a=readinput()
    ans=main(n,x,a)
    printans(ans)
