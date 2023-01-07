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
    # 右端 r を固定しながら左端 l を動かして条件をみたす(l, r)の組の数を数える
    l = 0
    count = 0
    for r in range(1, n):
        while l < r and a[r] - a[l] > k:
            l += 1
        count += r - l
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
