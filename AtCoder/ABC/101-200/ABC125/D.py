def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    sump=0
    summ=0
    minm=-10**9
    minp=10**9
    countm=0
    for i in range(n):
        if a[i]>=0:
            sump+=a[i]
            minp=min(minp,a[i])
        else:
            countm+=1
            summ+=a[i]
            minm=max(minm,a[i])
    #print(sump,summ,countm,minm,minp)
    if countm%2==0:
        return sump-summ
    else:
        return sump-summ-min(minp,abs(minm))*2

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)

    