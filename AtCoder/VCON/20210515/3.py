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
    n,k,m=m_input()
    a=l_input()
    return n,k,m,a

def main(n,k,m,a):
    mokuhyo = n*m
    need = mokuhyo - sum(a)
    if need <= k:
        return max(0, need)
    else:
        return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,m,a=readinput()
    ans=main(n,k,m,a)
    printans(ans)
