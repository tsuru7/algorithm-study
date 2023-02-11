def readinput():
    n,k=list(map(int,input().split()))
    p=list(map(int,input().split()))
    return n,k,p

def main(n,k,p):
    ps=sorted(p)
    sum=0
    for i in range(k):
        sum+=ps[i]
    
    return sum

if __name__=='__main__':
    n,k,p=readinput()
    ans=main(n,k,p)
    print(ans)
