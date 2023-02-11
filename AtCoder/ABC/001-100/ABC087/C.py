def readinput():
    n=int(input())
    a=[]
    l=list(map(int,input().split()))
    a.append(l)
    l=list(map(int,input().split()))
    a.append(l)
    return n,a

def main(n,a):
    s0=[0]*(n+1)
    s1=[0]*(n+1)
    for i in range(n):
        s0[i+1]=s0[i]+a[0][i]
        s1[i+1]=s1[i]+a[1][i]
    maxa=0
    for i in range(1,n+1):
        ame=s0[i]+s1[n]-s1[i-1]
        maxa=max(maxa,ame)
    return maxa

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
