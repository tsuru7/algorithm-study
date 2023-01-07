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
    # 左端 l を固定しながら右端 r を動かして条件をみたす(l, r)の組の数を数える
    ans = 0
    r = 0
    for l in range(n):
        while r < n and a[r] - a[l] <= k:
            r += 1
        else:
            r -= 1
        ans += r - l

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
