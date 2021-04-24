def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    sum=0
    h=a[0]
    for i in range(1,n):
        if h>a[i]:
            sum+=h-a[i]
        else:
            h=a[i]
    return sum

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
