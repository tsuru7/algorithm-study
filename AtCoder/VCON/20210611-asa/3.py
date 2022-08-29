import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from math import gcd
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
    x=l_input()
    return n,x


def main(n,x):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    ans = INFTY
    for i in range(1, 2**len(primes)):
        b = 1
        v = 1
        for j in range(len(primes)):
            if i & b == b:
                v *= primes[j]
            b *= 2
        for y in x:
            if gcd(y, v) == 1:
                break
        else:
            ans = min(ans, v)



    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x=readinput()
    ans=main(n,x)
    printans(ans)
