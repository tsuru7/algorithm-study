def readinput():
    n,k=list(map(int,input().split()))
    r=list(map(int,input().split()))
    return n,k,r

def main(n,k,r):
    rs=sorted(r)
    rate=0
    for i in range(n-k,n):
        rate=(rate+rs[i])/2
    return rate

if __name__=='__main__':
    n,k,r=readinput()
    ans=main(n,k,r)
    print(ans)
