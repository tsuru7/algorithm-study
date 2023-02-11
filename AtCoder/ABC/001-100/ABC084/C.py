def readinput():
    n=int(input())
    c=[0]
    s=[0]
    f=[0]
    for _ in range(1,n):
        l=list(map(int,input().split()))
        c.append(l[0])
        s.append(l[1])
        f.append(l[2])
    return n,c,s,f

def main(n,c,s,f):
    tList=[]
    t=[0]*(n+1)
    #print(s)
    #print(t)
    for e in range(1,n):
        t[e]=s[e]
        for i in range(e+1,n):
            t[i]=t[i-1]+c[i-1]
            if t[i]<=s[i]:
                t[i]=s[i]
            else:
                if t[i]%f[i]==0:
                    pass
                else:
                    t[i]=((t[i]//f[i])+1)*f[i]
        t[n]=t[n-1]+c[n-1]
        tList.append(t[n])
    tList.append(0)
    return tList

if __name__=='__main__':
    n,c,s,f=readinput()
    ans=main(n,c,s,f)
    for t in ans:
        print(t)
