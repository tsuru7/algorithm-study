import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict

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
    return n,a

def solve(n,a):
    MOD = 10**9+7
    a_fact = [myFactorization(a[i]) for i in range(n)]
    lcm_dict = defaultdict(int)
    for factList in a_fact:
        for prime, exp in factList:
            lcm_dict[prime] = max(lcm_dict[prime], exp)
    lcm = 1
    for prime, exp in lcm_dict.items():
        for i in range(exp):
            lcm *= prime
            lcm %= MOD
    # print(f'lcm(MOD): {lcm}')
    
    b = [0 for _ in range(n)]
    sum = 0
    for i in range(n):
        inv_ai = pow(a[i], MOD-2, MOD)
        b[i] = (lcm*inv_ai) % MOD
        sum += b[i]
        sum %= MOD
    return sum

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
