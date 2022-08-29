import sys
sys.setrecursionlimit(10**6)
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
    t,a=m_input()
    h=l_input()
    return n,t,a,h

def main(n,t,a,h):
    ans=0
    minh = INFTY
    for i in range(n):
        temp = t*1000 - h[i]*6
        if abs(a*1000-temp) < minh:
            ans = i
            minh = abs(a*1000-temp)
    return ans+1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,t,a,h=readinput()
    ans=main(n,t,a,h)
    printans(ans)
