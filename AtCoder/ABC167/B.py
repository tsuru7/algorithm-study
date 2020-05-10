def readinput():
    a,b,c,k = list(map(int,input().split()))
    return a,b,c,k

def main(a,b,c,k):
    if(a>=k):
        return k
    k2=k-a
    if(b>=k2):
        return a
    k3=k2-b
    return a-k3
    

if __name__=='__main__':
    a,b,c,k=readinput()
    ans=main(a,b,c,k)
    print(ans)
