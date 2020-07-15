def readinput():
    h,w=list(map(int,input().split()))
    n=int(input())
    a=list(map(int,input().split()))
    return h,w,n,a

def main(h,w,n,a):
    cmat=[]
    for _ in range(h):
        cmat.append([0]*w)
    i=0
    j=0
    jstep=1
    for c in range(n):
        k=a[c]
        while k>0: 
            cmat[i][j]=c+1
            if (j==0 and jstep==-1) or (j==w-1 and jstep==1):
                i=i+1
                jstep=jstep*(-1)
            else:
                j=j+jstep
            k-=1
    return cmat

if __name__=='__main__':
    h,w,n,a=readinput()
    ans=main(h,w,n,a)
    for i in range(h):
        print(' '.join(map(str,ans[i])))

            