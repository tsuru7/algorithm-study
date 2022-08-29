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
    l,h=m_input()
    n = i_input()
    alist = []
    for _ in range(n):
        alist.append(i_input())
    return l,h,n,alist

def main(l,h,n,alist):
    ans=[]
    for a in alist:
        if a < l:
            ans.append(l-a)
        elif a > h:
            ans.append(-1)
        else:
            ans.append(0)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    l,h,n,alist=readinput()
    ans=main(l,h,n,alist)
    printans(ans)
