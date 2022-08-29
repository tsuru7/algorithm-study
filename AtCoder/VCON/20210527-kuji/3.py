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
    alist = []
    for _ in range(n):
        alist.append(i_input())
    return n,alist

def main(n,alist):
    alist.insert(0,0)
    lit = 1
    for i in range(n):
        lit = alist[lit]
        if lit == 2:
            return i+1
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,alist=readinput()
    ans=main(n,alist)
    printans(ans)
