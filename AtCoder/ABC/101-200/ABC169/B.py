INFTY=10**18

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    if(a.count(0)!=0):
        return 0
        
    res=a[0]
    for i in range(1,n):
        res*=a[i]
        if res>INFTY:
            return -1
    return res

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
