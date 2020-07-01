import math
def readinput():
    a,b=list(map(int,input().split()))
    return a,b

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

def euclid(x,y):
    if x<y:
        x,y=y,x
    
    while y>0:
        r=x%y
        x=y
        y=r
    return x

def main(a,b):
    gcd=euclid(a,b)
    factList=myFactorization(gcd)
    return len(factList)+1

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    print(ans)
