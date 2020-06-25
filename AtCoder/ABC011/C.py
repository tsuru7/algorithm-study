def readinput():
    n=int(input())
    ng1=int(input())
    ng2=int(input())
    ng3=int(input())
    return n,ng1,ng2,ng3

def main(n,ng1,ng2,ng3):
    if ng1==n or ng2==n or ng3==n:
        return 'NO'
    ngs=sorted([ng1,ng2,ng3])
    if ngs[1]==ngs[0]+1 and ngs[2]==ngs[1]+1:
        return 'NO'
    
    if n==300:
        if ng1%3==0 or ng2%3==0 or ng3%3==0:
            return 'NO'
        else:
            return 'YES'
    if n==299:
        for i in range(0,100):
            if 3*i+2 in [ng1,ng2,ng3]:
                pass

    if 290<=n and n<=299:
        pass

def main2(n,ng1,ng2,ng3):
    if n in [ng1,ng2,ng3]:
        return 'NO'
    next=n
    count=0
    while(next>3):
        if next-3 in [ng1,ng2,ng3]:
            if next-2 in [ng1,ng2,ng3]:
                if next-1 in [ng1,ng2,ng3]:
                    return 'NO'
                else:
                    next=next-1
            else:
                next=next-2
        else:
            next=next-3
        count+=1
    else:
        count+=1
    if count>100:
        return 'NO'
    else:
        return 'YES'

import sys
INFTY=sys.maxsize
def main3(n,ng1,ng2,ng3):
    dp=[INFTY]*(n+1)
    if n in [ng1,ng2,ng3]:
        return 'NO'
    dp[n]=0
    for i in range(n,-1,-1):
        if i in [ng1,ng2,ng3]:
            continue
        for j in range(1,4):
            if i-j <0:
                break
            dp[i-j]=min(dp[i]+1,dp[i-j])
    if dp[0]<=100:
        return 'YES'
    else:
        return 'NO'


if __name__=='__main__':
    n,ng1,ng2,ng3=readinput()
    ans=main3(n,ng1,ng2,ng3)
    print(ans)
