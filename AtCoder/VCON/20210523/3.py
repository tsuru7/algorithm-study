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
    stlist = []
    for _ in range(n):
        s, t = input().split()
        t = int(t)
        stlist.append((s,t))
    x=input()
    return n,stlist,x

def main(n,stlist,x):
    sleep = False
    ans=0
    for s, t in stlist:
        if sleep:
            ans += t
        if s == x:
            sleep = True
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,stlist,x=readinput()
    ans=main(n,stlist,x)
    printans(ans)
