import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    a=l_input()
    b=l_input()
    c=l_input()
    return n,a,b,c

def main(n,a,b,c):
    a.sort()
    b.sort()
    c.sort()
    printd(f'a: {a}')
    printd(f'b: {b}')
    printd(f'c: {c}')

    ans = 0
    for j in range(n):
        x = b[j]
        i = bisect_left(a, x)
        k = bisect_right(c, x)
        # print(f'x: {x}, i: {i}, k: {k}')
        ans += i*(n-k)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=main(n,a,b,c)
    printans(ans)
