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

def solve(n,k,a):
    b = [ [] for _ in range(k) ]
    for i in range(n):
        j = i % k
        b[j].append(a[i])
    for j in range(k):
        b[j].sort()
    c = []
    for i in range(n):
        l, j = divmod(i, k)
        c.append(b[j][l])
    a.sort()
    if a == c:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
