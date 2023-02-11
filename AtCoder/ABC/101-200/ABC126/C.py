def readinput():
    n,k=map(int,input().split())
    return n,k

def main(n,k):
    ans=0
    for i in range(1,n+1):
        p=1/n
        point=i
        while(point<k):
            point*=2
            p/=2
        #print(p)
        ans+=p
    return ans

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    print(ans)
