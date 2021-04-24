def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    l=1
    count=0
    comb=0
    for i in range(1,n):
        if a[i-1]<a[i]:
            l+=1
            if l==2:
                comb=1
            else:
                comb=comb+(l-1)
        else:
            count+=comb
            comb=0
            l=1
    count+=comb
    return count+n

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
