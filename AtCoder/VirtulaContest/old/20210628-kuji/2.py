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
    n,x=m_input()
    a=l_input()
    return n,x,a

def main(n,x,a):
    if sum(a) == x:
        return n

    a.sort()
    i = 0
    while i < n and x >= a[i]:
        x -= a[i]
        i += 1
    if x > 0 and i > 0:
        i -= 1
    return i

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,a=readinput()
    ans=main(n,x,a)
    printans(ans)
