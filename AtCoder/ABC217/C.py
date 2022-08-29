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
    p=l_input()
    return n,p

def main(n,p):
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    return q

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
