def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    #print(a)
    a.sort(reverse=True)
    #print(a)
    sum=a[0]
    j=0
    k=1
    for i in range(2,n):
        sum+=a[k]
        #print(a[k])
        j+=1
        if j==2:
            j=0
            k+=1
    return sum

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
