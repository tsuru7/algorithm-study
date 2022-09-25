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
    n,k=m_input()
    a=l_input()
    return n,k,a

def judge(wj, k, a):
    n = len(a)
    count = 0
    for i in range(n):
        count += min(a[i], wj)
    if count <= k:
        return True
    else:
        return False

def solve(n,k,a):
    ac = 0
    wa = k + 1
    while wa - ac > 1:
        wj = (ac + wa)//2
        if judge(wj, k, a):
            ac = wj
        else:
            wa = wj
    
    for i in range(n):
        k -= min(ac, a[i])
        a[i] = max(0, a[i]-ac)
    for i in range(n):
        if k > 0 and a[i] > 0:
            a[i] -= 1
            k -= 1
    return a

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
