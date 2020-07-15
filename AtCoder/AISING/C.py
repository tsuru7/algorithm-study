from math import sqrt

def readinput():
    n=int(input())
    return n

def main(n):
    f=[0]*n
    for i in range(1,n+1):
        sqrt2n=int(sqrt(2*i))+1
        #print(i,sqrt2n)
        for x in range(1,sqrt2n):
            for y in range(1,sqrt2n-x+1):
                if (x+y)**2>2*i:
                    break
                for z in range(1,sqrt2n-x+1):
                    v=(x+y)**2+(y+z)**2+(z+x)**2
                    if v>2*i:
                        break
                    #print(v)
                    if v==2*i:
                        f[i-1]+=1
                        #print('found')
                        #print(x,y,z,i)
    return f

def F(x,y,z):
    return ((x+y)**2+(y+z)**2+(z+x)**2)//2

def main2(n):
    sqrt2n=int(sqrt(2*n))+1
    cntbl=[0]*(10**4+1)
    for x in range(1,sqrt2n):
        for y in range(1,sqrt2n):
            for z in range(1,sqrt2n):
                v=F(x,y,z)
                if v>n:
                    break
                cntbl[v]+=1
    return cntbl


if __name__=='__main__':
    n=readinput()
    ans=main2(n)
    for i in range(1,n+1):
        print(ans[i])
