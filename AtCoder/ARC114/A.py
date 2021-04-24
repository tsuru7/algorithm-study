from math import gcd
import sys
INFTY = sys.maxsize
from collections import deque

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

import math
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
    n=i_input()
    a=l_input()
    return n,a

def minfact(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i
    

def main(n,a):
    y = []
    facts = myFactorization(a[0])
    for f in facts:
        y.append({f[0]})
    # print(y)

    for i in range(1, n):
        prevy = y
        y = []
        facts = myFactorization(a[i])
        for cand in prevy:
            added = False
            for f in facts:
                temp = cand.copy()
                # print(f, temp)
                if f[0] in temp:
                    if added == False:
                        y.append(temp)
                        # print(y, temp, id(temp))
                        added = True
                    # print('continue')
                    continue
                temp.add(f[0])
                y.append(temp)
                # print(y, temp, id(temp))
    ans = INFTY
    for cand in y:
        prod = 1
        for c in cand:
            prod *= c
        ans = min(ans, prod)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
