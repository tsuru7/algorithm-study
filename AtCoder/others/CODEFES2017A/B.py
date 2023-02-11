def readinput():
    n,m,k=list(map(int,input().split()))
    return n,m,k

def main(n,m,k):
    for x in range(0,m+1):
        for y in range(0,n+1):
            if (n-y)*x+y*(m-x)==k:
                return 'Yes'
    return 'No'

if __name__=='__main__':
    n,m,k=readinput()
    ans=main(n,m,k)
    print(ans)
