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

def solve(n):
    divisor = set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisor.add(i)
            divisor.add(n//i)
        i += 1
    ans=set()
    for d in list(divisor):
        if d == 1:
            continue
        x = n
        while x % d == 0:
            x //= d
        if x % d == 1:
            ans.add(d)
    x = n-1
    i = 1
    while i*i <= x:
        if x % i == 0:
            ans.add(i)
            ans.add(x//i)
        i += 1
    


    return len(ans) - 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
