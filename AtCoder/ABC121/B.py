def readinput():
    n,m,c=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=[]
    for _ in range(n):
        l=list(map(int,input().split()))
        a.append(l)
    return n,m,a,b,c

def main(n,m,a,b,c):
    seikai=0
    for i in range(n):
        sum=0
        for j in range(m):
            sum+=a[i][j]*b[j]
        sum+=c
        if sum > 0:
            seikai+=1
    return seikai

if __name__=='__main__':
    n,m,a,b,c=readinput()
    ans=main(n,m,a,b,c)
    print(ans)

