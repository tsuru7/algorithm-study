import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    return n

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

def main(n):
    if n == 1:
        return 'Not Prime'

    if isPrime(n):
        return 'Prime'
    
    sum = 0
    x = n % 10
    if (x % 2 == 0) or (x == 5):
        return 'Not Prime'
    sum += x
    n = n // 10
    while n > 0:
        x = n % 10
        sum += x
        n = n // 10
    if sum % 3 == 0:
        return 'Not Prime'
    
    return 'Prime'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
