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
    n,w=m_input()
    a=l_input()
    return n,w,a

def solve(n,w,a):
    candidate = set()
    for i in range(n):
        candidate.add(a[i])
    for i in range(n):
        for j in range(i+1, n):
            candidate.add(a[i]+a[j])
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                candidate.add(a[i]+a[j]+a[k])
    ans=0
    for i in range(1, w+1):
        if i in candidate:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,w,a=readinput()
    ans=solve(n,w,a)
    printans(ans)
