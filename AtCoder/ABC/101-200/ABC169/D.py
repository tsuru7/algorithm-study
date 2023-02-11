def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

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
    n=int(input())
    return n

def possibleCnt(n):
    cnt=0
    resu=n
    for i in range(1,n+1):
        if resu >= i:
            cnt+=1
            resu-=i
            #print(cnt,resu)
    return cnt       

def main(n):
    #ansList=factorization(n)
    ansList=myFactorization(n)
    #print(ansList)
    count=0
    for l in ansList:
        if(l[0]!=1):
            count+=possibleCnt(l[1])
    return count    


if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)

