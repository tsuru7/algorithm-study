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
    n,m=m_input()
    a=l_input()
    return n,m,a

def solve(n,m,a):
    if n == 1:
        return 0

    a.sort()
    b = []
    zero = True
    if a[0] > 0:
        zero = False
    acc = a[0]
    for i in range(1, n):
        if a[i] == a[i-1] or a[i] == a[i-1]+1:
            acc += a[i]
        else:
            b.append(acc)
            acc = a[i]
    b.append(acc)
    if a[-1] == m-1 and zero:
        b[0] += b[-1]
        b = b[:-1]
    
    b.sort(reverse=True)
    ans = sum(b[1:])
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
