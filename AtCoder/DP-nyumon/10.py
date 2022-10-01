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
    b = l_input()
    return n,k,a,b

def solve(n,k,a,b):
    dp_a = [False for _ in range(n)]
    dp_b = [False for _ in range(n)]
    dp_a[0] = True
    dp_b[0] = True
    for i in range(1, n):
        a0 = a[i-1]
        a1 = a[i]
        b0 = b[i-1]
        b1 = b[i]
        dp_a[i] |= dp_a[i-1] and (abs(a0-a1) <= k)
        dp_a[i] |= dp_b[i-1] and (abs(b0-a1) <= k)
        dp_b[i] |= dp_a[i-1] and (abs(a0-b1) <= k)
        dp_b[i] |= dp_b[i-1] and (abs(b0-b1) <= k)
    if dp_a[-1] | dp_b[-1]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a,b=readinput()
    ans=solve(n,k,a,b)
    printans(ans)
