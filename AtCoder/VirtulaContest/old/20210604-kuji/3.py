import sys
sys.setrecursionlimit(10**5)
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
    n,k,s=m_input()
    return n,k,s

def main(n,k,s):
    if k == 0:
        if s < 10**9:
            a = [s+1]*n
        else:
            a = [1]*n
        return a
        
    l = n - k + 1
    a = [0]*n
    for i in range(l-1):
        a[i] = s//l
    a[l-1] = s - (s//l)*(l-1)
    for i in range(l, n):
        a[i] = a[i-l]
    return a

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    n,k,s=readinput()
    ans=main(n,k,s)
    printans(ans)
