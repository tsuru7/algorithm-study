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
    return n

def isprime(x):
    ans = True
    i = 2
    while i*i <= x:
        if x % i == 0:
            ans = False
            break
        i += 1
    return ans

def solve(n):
    ans=[]
    for i in range(2, n+1):
        if isprime(i):
            ans.append(i)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
