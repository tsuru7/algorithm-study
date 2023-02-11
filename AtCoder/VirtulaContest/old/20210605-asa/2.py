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
    n=i_input()
    return n

def main(n):
    if isPrime(n):
        return 'YES'
    else:
        return 'NO'

import math

def isPrime(n):
    if n==2:
        return True

    if n<=1 or n%2==0:
        return False

    m = int(math.sqrt(n))+1
    for i in range(3,m,2):
        if n % i == 0:
            return False
    return True

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
