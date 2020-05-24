def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def countingSort(n,a,k):
    c=[0]*(k+1)
    for i in range(n):
        c[a[i]]+=1
    for i in range(1,k+1):
        c[i]=c[i]+c[i-1]
    b=[0]*n
    for j in range(n-1,-1,-1):
        b[c[a[j]]-1]=a[j]
        c[a[j]]-=1
    return b

def main(n,a):
    b=countingSort(n,a,10000)
    return b 
    
if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(' '.join(map(str,ans)))
