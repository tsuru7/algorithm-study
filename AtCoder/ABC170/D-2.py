def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    maxa=10**6
    isprime=[True]*(maxa+1)
    sa=sorted(a)

    prevx=0
    for x in sa:
        if isprime[x]==False:
            continue
        if prevx==x:
            isprime[x]=False
            continue

        i=x*2
        while(i<=maxa):
            isprime[i]=False
            i+=x
        prevx=x
    
    count=0
    for x in sa:
        if isprime[x]==True:
            count+=1
    return count

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
