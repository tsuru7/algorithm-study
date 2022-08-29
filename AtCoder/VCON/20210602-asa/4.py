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

def main(n,a):
    tmp = a[0]
    for i in range(1, n):
        tmp = math.gcd(tmp, a[i])
    if tmp != 1:
        return 'not coprime'
    fact = set()
    for i in range(n):
        tmp = myFactorization(a[i])
        for prime, ext in tmp:
            if prime == 1:
                continue
            if prime in fact:
                return 'setwise coprime'
            else:
                fact.add(prime)
    return 'pairwise coprime'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
