def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    return n,a,b

def main(n,a,b):
    sum=0
    for i in range(n):
        hp=b[i]
        use0=min(hp,a[i])
        a[i]-=use0
        hp-=use0
        sum+=use0
        if hp>0:
            use1=min(hp,a[i+1])
            a[i+1]-=use1
            sum+=use1
    
    return sum

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    print(ans)
