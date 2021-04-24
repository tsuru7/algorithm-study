def readinput():
    n,k=map(int,input().split())
    return n,k

def main(n,k):
    if n>k:
        n=n%k+k
        n=min(n,abs(n-k))
    return min(n,abs(n-k))

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    print(ans)
