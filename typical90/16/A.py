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
    a,b,c=m_input()
    return n,a,b,c

def solve(n,a,b,c):
    ans=INFTY
    for i in range(10000):
        for j in range(10000):
            if i+j > 9999:
                break
            k = n-a*i-b*j
            if k % c == 0 and 0 <= k//c <= 9999:
                ans = min(ans, i+j+k//c)
            
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=solve(n,a,b,c)
    printans(ans)
