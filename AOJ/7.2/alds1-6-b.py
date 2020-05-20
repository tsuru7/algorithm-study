def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if(a[j]<=x):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1

def main(n,a):
    ans=partition(a,0,n-1)
    print(' '.join(map(str,a[:ans])),end='')
    print(' ['+str(a[ans])+'] ',end='')
    if(ans<n-1):
        print(' '.join(map(str,a[ans+1:])))

    return

if __name__=='__main__':
    n,a=readinput()
    main(n,a)
