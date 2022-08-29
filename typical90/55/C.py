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
    n,p,q=m_input()
    a=l_input()
    return n,p,q,a

def solve(n,p,q,a):
    ans=0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for m in range(l+1, n):
                        if (((a[i]*a[j]%p)*a[k]%p)*a[l]%p)*a[m]%p == q:
                            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p,q,a=readinput()
    ans=solve(n,p,q,a)
    printans(ans)
