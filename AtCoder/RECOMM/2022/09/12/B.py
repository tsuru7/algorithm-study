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
    a = [i_input() for _ in range(n)]
    return n,a

def solve(n,a):
    a.sort(reverse=True)
    # case1
    # p1 - 2p2 + 2p3 - 2p4 ...
    plus = True
    p1 = 1
    m1 = 0
    p2 = 0
    m2 = 0
    for i in range(1, n-1):
        plus = not plus
        if plus:
            p2 += 1
        else:
            m2 += 1
    plus = not plus
    if plus:
        p1 += 1
    else:
        m1 += 1
    ans1 = 0
    for i in range(p2):
        ans1 += 2*a[i]
    for i in range(p2, p2+p1):
        ans1 += a[i]
    for i in range(m2):
        ans1 -= 2*a[-(i+1)]
    for i in range(m2, m2+m1):
        ans1 -= a[-(i+1)]

    # case2
    # -p1 + 2p2 - 2p3 + 2p4 ...
    plus = False
    p1 = 0
    m1 = 1
    p2 = 0
    m2 = 0
    for i in range(1, n-1):
        plus = not plus
        if plus:
            p2 += 1
        else:
            m2 += 1
    plus = not plus
    if plus:
        p1 += 1
    else:
        m1 += 1
    ans2 = 0
    for i in range(p2):
        ans2 += 2*a[i]
    for i in range(p2, p2+p1):
        ans2 += a[i]
    for i in range(m2):
        ans2 -= 2*a[-(i+1)]
    for i in range(m2, m2+m1):
        ans2 -= a[-(i+1)]        

    return max(ans1, ans2)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
