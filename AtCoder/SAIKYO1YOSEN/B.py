def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,k,a

def main(n,k,a):
    MOD=10**9+7

    t=0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                t+=1
    
    s=0
    for i in range(n):
        for j in range(n):
            if a[j]<a[i]:
                s+=1
    
    x= ( (k*t)%MOD + ((k*(k-1)//2)%MOD)*s%MOD  )%MOD

    return x

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    print(ans)

