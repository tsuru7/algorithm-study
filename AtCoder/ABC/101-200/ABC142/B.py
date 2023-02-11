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
    n,k=m_input()
    h=l_input()
    return n,k,h

def main(n,k,h):
    ans=0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,h=readinput()
    ans=main(n,k,h)
    printans(ans)
