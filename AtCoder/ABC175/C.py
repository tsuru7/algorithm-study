def readinput():
    x,k,d=map(int,input().split())
    return x,k,d

def main(x,k,d):
    x=abs(x)
    q=x//d
    r=x%d
    if k<q:
        ans=x-k*d
    else:
        if (k-q)%2==0:
            ans=r
        else:
            ans=d-r
    return ans

if __name__=='__main__':
    x,k,d=readinput()
    ans=main(x,k,d)
    print(ans)
