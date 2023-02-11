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
    n,k,q=m_input()
    a=l_input()
    l=l_input()
    return n,k,q,a,l

def solve(n,k,q,a,l):
    for i in l:
        i -= 1
        # print(f'i: {i}')
        if i == k-1:
            a[i] = min(n, a[i]+1)
            continue
        elif a[i+1] == a[i]+1:
            continue
        else:
            a[i] += 1
    return a

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,k,q,a,l=readinput()
    ans=solve(n,k,q,a,l)
    printans(ans)
