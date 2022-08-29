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
    n,k,x=m_input()
    a=l_input()
    return n,k,x,a

def solve(n,k,x,a):
    for i in range(n):
        ai = a[i]
        p = ai // x
        if k >= p:
            a[i] -= p*x
            k -= p
        else:
            a[i] -= k*x
            k = 0
    if k == 0:
        ans = sum(a)
    else:
        a.sort(reverse=True)
        i = 0
        while k > 0 and i < n:
            a[i] = 0
            k -= 1
            i += 1
        ans = sum(a)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,x,a=readinput()
    ans=solve(n,k,x,a)
    printans(ans)
