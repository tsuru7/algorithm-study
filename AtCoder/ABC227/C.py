import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import sqrt
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
    return n

def main(n):
    m1 = int(pow(n, 1/3))+1
    m2 = int(sqrt(n))+1
    # print(m)
    ans=0
    for a in range(1, m1+1):
        for b in range(a, m2+1):
            cmax = n // (a*b)
            if cmax < b:
                break
            # print(f'a: {a}, b: {b}, c: {cmax}, abc: {a*b*cmax}')
            ans += cmax -b +1
            # print(cmax-b+1)
    return ans

def main2(n):
    ans = 0
    for a in range(1, n+1):
        counta = 0
        for b in range(a, n+1):
            countb = 0
            for c in range(b, n+1):
                if a*b*c <= n:
                    ans += 1
                    countb += 1
                else:
                    break
            if countb > 0:
                print(a, b, c, countb)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
    # ans=main2(n)
    # printans(ans)
