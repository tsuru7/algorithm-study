def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    a.insert(0,0)
    b=[0]*(n+1)
    for i in range(n,0,-1):
        sum=0
        j=i*2
        while(j<=n):
            sum+=b[j]
            j+=i
        b[i]=(a[i]-(sum%2)+2)%2
    #print(b)
    ans=[]
    for i in range(1,n+1):
        if b[i]!=0:
            ans.append(i)
    return ans

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(len(ans))
    if len(ans)>0:
        print(' '.join(map(str,ans)))
