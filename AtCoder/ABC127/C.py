def readinput():
    n,m=map(int,input().split())
    l=[]
    r=[]
    for i in range(m):
        li,ri=map(int,input().split())
        l.append(li)
        r.append(ri)
    return n,m,l,r

def main(n,m,l,r):
    lmax=1
    rmin=n
    for i in range(m):
        lmax=max(lmax,l[i])
        rmin=min(rmin,r[i])
    return max(rmin-lmax+1,0)

if __name__=='__main__':
    n,m,l,r=readinput()
    ans=main(n,m,l,r)
    print(ans)
