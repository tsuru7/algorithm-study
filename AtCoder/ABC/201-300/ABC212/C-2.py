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
    b=l_input()
    return n,m,a,b

def main(n,m,a,b):
    a.sort()
    b.sort()
    ans=INFTY
    ai = 0
    bi = 0
    while ai < n and bi < m:
        ans = min(ans, abs(a[ai] - b[bi]))
        if a[ai] < b[bi]:
            ai += 1
        else:
            bi += 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a,b=readinput()
    ans=main(n,m,a,b)
    printans(ans)
