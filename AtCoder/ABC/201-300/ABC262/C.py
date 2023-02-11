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
    a=l_input()
    return n,a

def solve(n,a):
    ans=0
    count = 0
    for i in range(n):
        if a[i] == i+1:
            count += 1
    ans += count*(count-1)//2
    for i in range(n):
        if a[i] != i+1:
            j = a[i]-1
            if j > i and a[j] == i+1:
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
