import sys
sys.setrecursionlimit(10**6)
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

import math
def myDivisors(n):
    '''nの約数を列挙する

    戻り値: divisors (set)
    '''

    divisors=set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
        i += 1
    return divisors

def myFactorization(n):
    '''nを素因数分解する

    戻り値: factList = [[prime1, exp1], [prime2, exp2],...] 
           n=(prime1)**exp1 * (prime2)**exp2 * ...
    '''

    factList=[]
    temp=n
    cnt=0
    while(temp%2==0):
        temp=temp//2
        cnt+=1
    if(cnt>0):
        factList.append([2,cnt])

    m=int(math.sqrt(n))+1
    for i in range(3,m+1,2):
        cnt=0
        while(temp%i==0):
            temp=temp//i
            cnt+=1
        if(cnt>0):
            factList.append([i,cnt])
        if(temp==1):
            break
    if(temp>1):
        factList.append([temp,1])
    return factList

def readinput():
    n,m=m_input()
    a=l_input()
    return n,m,a

def main(n,m,a):
    done = {1}
    candidates = [True]*(m+1)
    a.sort()
    for ai in a:
        factList = myFactorization(ai)
        for fact, _ in factList:
            if fact in done:
                continue
            tmp = fact
            while tmp <= m:
                candidates[tmp] = False
                tmp += fact
            done.add(fact)

    ans=[]
    for i in range(1, m+1):
        if candidates[i]:
            ans.append(i)

    return ans

def printans(ans):
    print(len(ans))
    for a in ans:
        print(a)

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    printans(ans)
