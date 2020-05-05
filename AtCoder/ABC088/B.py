def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return (n,a)

def main(n,a):
    a.sort(reverse=True)
    nloop=n//2
    apoint=0
    bpoint=0
    l=0
    while(l<nloop):
        apoint+=a[l*2]
        bpoint+=a[l*2+1]
        l+=1
    if(n%2==1):
        apoint+=a[n-1]
    return apoint-bpoint


if __name__=='__main__':
    n,a = readinput()
    ans=main(n,a)
    print(ans)
