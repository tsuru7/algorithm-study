from sympy import divisors
from math import gcd

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    M=[]
    for _ in range(n):
        M.append([0]*n)
    
    for i in range(n):
        for j in range(i,n):
            if(gcd(a[i], a[j])==1):
                M[i][j]=1
                M[j][i]=1
            else:
                M[i][j]=0
                M[j][i]=0
    count=0
    for i in range(n):
        if(sum(M[i])==n-1):
            count+=1
    return count


    divisorsList=[]
    for i in range(n):
        divisorsList.append(divisors(a[i]))




    sortedA=sorted(a)
    #m=int(sqrt(sortedA[n-1]))+1
    m=sortedA[n-1]//2+1
    #print(sortedA)
    #print(m)

    count=0
    for i in range(n):
        calc=False
        for j in range(n):
            if i==j:
                continue
            if sortedA[j]>m:
                #print(i,j)
                continue
            if(sortedA[i]%sortedA[j]==0):
                #print(i,j)
                break
            else:
                calc=True
        else:
            if calc==True:
                count+=1

    return count

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
