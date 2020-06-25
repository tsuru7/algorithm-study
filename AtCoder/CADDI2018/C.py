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
    n,p=list(map(int,input().split()))
    return n,p

def main(n,p):
    factList=myFactorization(p)
    gcd=1
    for fact in factList:
        gcd=gcd*fact[0]**(fact[1]//n)
    return gcd

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    print(ans)
