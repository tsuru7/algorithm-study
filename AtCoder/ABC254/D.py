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
    ans=0
    checked = set()
    for i in range(1, n+1):
        if i in checked:
            continue
        x = 1
        count = 0
        while i*x*x <= n:
            count += 1
            checked.add(i*x*x)
            x += 1
        ans += count*count

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
