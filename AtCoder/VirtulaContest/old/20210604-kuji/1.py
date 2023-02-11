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
    d=l_input()
    return n,d

def main(n,d):
    ans=0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += d[i]*d[j]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d=readinput()
    ans=main(n,d)
    printans(ans)
