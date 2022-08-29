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
    n,k=m_input()
    return n,k

def main(n,k):
    ans=0
    for fl in range(1,n+1):
        for ro in range(1, k+1):
            ans += fl*100 + ro
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    printans(ans)
