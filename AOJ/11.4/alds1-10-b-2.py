import sys
INFTY=sys.maxsize

def main(n,m,p):
    #global m
    #global p

    for i in range(1,n+1):
        m[i][i]=0

    for l in range(1,n):
        for i in range(1,n-l+1):
            j=i+l
            m[i][j]=INFTY
            for k in range(i,j):
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j]+p[i-1]*p[k]*p[j])    
    print(m[1][n])


n=int(input())
p=[]
k,l=list(map(int,input().split()))
i=1
p.append(k)
p.append(l)
while(i<n):
    l,m=list(map(int,input().split()))
    p.append(m)
    i+=1

m=[]
for i in range(n+1):
    mm=[0]*(n+1)
    m.append(mm)

main(n,m,p)
