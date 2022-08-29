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
    n,m=m_input()
    return n,m

def main(n,m):
    aka = 0
    oto = 0
    for rou in range(n+1):
        ashi = m - 3*rou
        if ashi % 2 == 1:
            continue
        aka = (ashi - (n-rou)*2)//2
        oto = n - rou - aka
        if aka >= 0 and oto >=0:
            return (oto, rou, aka)
    return (-1, -1, -1)

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    n,m=readinput()
    ans=main(n,m)
    printans(ans)
