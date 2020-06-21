def readinput():
    a,b,n=list(map(int,input().split()))
    return a,b,n

def main(a,b,n):
    m=int(min(b,n)*a/b)+1
    maxdif=0
    for xx in range(0,m):
        if b*xx%a==0:
            x=b*xx//a
        else:
            x=int(b/a*xx)+1
        maxdif=max(maxdif,int(a*x/b)-a*int(x/b))
    return maxdif

if __name__=='__main__':
    a,b,n=readinput()
    ans=main(a,b,n)
    print(ans)
