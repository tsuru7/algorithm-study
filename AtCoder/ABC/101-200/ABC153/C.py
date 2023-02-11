def readinput():
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    return n,k,h

def main(n,k,h):
    if k>=n:
        return 0
    
    h.sort(reverse=True)
    ans=0
    for i in range(k,n):
        ans+=h[i]
    return ans

if __name__=='__main__':
    n,k,h=readinput()
    ans=main(n,k,h)
    print(ans)
