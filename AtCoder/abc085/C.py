def readinput():
    n,y=list(map(int,input().split()))
    return (n,y)

def main(n,y):
    k=0 # num of \10000
    l=0 # num of \5000
    m=0 # num of \1000
    # k+l+m must be n
    kmax=y//10000
    for kk in range(kmax+1):
        res1=y-10000*kk
        lmax=res1//5000
        for ll in range(lmax+1):
            res2=res1-5000*ll
            m=res2//1000
            if(kk+ll+m==n):
                return (kk,ll,m)
    return(-1,-1,-1)

if __name__=='__main__':
    n,y=readinput()
    k,l,m=main(n,y)
    print(' '.join(map(str,(k,l,m))))
