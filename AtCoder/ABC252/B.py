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
    b=l_input()
    return n,k,a,b

def solve(n,k,a,b):
    ab = [ [a[i], False] for i in range(n) ]
    for i in range(k):
        ab[b[i]-1][1] = True
    ab.sort(reverse=True)
    ans=ab[0][1]
    return 'Yes' if ans else 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a,b=readinput()
    ans=solve(n,k,a,b)
    printans(ans)
