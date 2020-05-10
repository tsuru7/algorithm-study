def readinput():
    n,m,x=list(map(int,input().split()))
    dat=[]
    for i in range(n):
        s=list(map(int,input().split()))
        c=s[0]
        a=s[1:]
        dat.append((c,a))
    return n,m,x,dat

def makeTableA(dat,n,m):
    tbl=[[0]*m]*n
    #print(n,len(tbl),m,len(tbl[0]))
    for i in range(n):
        tup=dat[i]
        a=tup[1]
        #print(a)
        #for j in range(m):
        #    tbl[i][j]=a[j]
        tbl[i]=list(a) 
        #print(tbl) 
    return tbl  

def main(n,m,x,dat):
    tblA=makeTableA(dat,n,m)
    #print(tblA)
    tblB=[[0]*(m+2)]*2**n  #
    #print(n,m,len(tblB), len(tblB[0]))  
    for i in range(2**n):
        tblB[i]=[0]*(m+2)
        b=1
        for j in range(n):
            if(i&b==b):
                for k in range(m):
                    #print(j,k)
                    tblB[i][k]+=tblA[j][k]
                    #print(tblB)
                tblB[i][m]+=dat[j][0]
                #print(tblB)
            b=b*2
        tblB[i][m+1]=min(tblB[i][0:m])
        #print(tblB)
    #print(tblB)
    # テーブルをスキャンする
    Pmin=12*10**5+1
    for i in range(2**n):
        if(tblB[i][m+1]>=x):
            price=tblB[i][m]
            if(price < Pmin):
                Pmin=price
    if(Pmin==12*10**5+1):
        Pmin=-1
    return Pmin


if __name__=='__main__':
    n,m,x,dat=readinput()
    ans=main(n,m,x,dat)
    print(ans)
