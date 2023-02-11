from bisect import bisect_left, bisect_right

def readinput():
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=[]
    c=[]
    for _ in range(m):
        bb,cc=list(map(int,input().split()))
        b.append(bb)
        c.append(cc)
    return n,m,a,b,c

def main(n,m,a,b,c):
    a.sort()
    for i in range(m):
        #print(a)
        bi=b[i]
        ci=c[i]
        j=bisect_left(a,ci)-1
        if j<0:
            continue
        if j>bi-1:
            save=a[bi:j+1]
            l=j-bi+1
            r=j
            a[l:r+1]=[ci]*(r-l+1)
            a[0:l]=save
        else:
            l=0
            r=j
            a[l:r+1]=[ci]*(r-l+1)

    sum=0
    for i in range(n):
        sum+=a[i]
    
    return sum

def main2(n,m,a,b,c):
    all=[]
    for i in range(n):
        all.append((a[i],1))
    for i in range(m):
        all.append((c[i],b[i]))
    all.sort(reverse=True, key=lambda x:x[0])
    #print(all)
    count=n
    sum=0
    i=0
    while(count>0):
        ni=all[i][1]
        if ni<=count:
            sum+=all[i][0]*ni
            count-=ni
        else:
            sum+=all[i][0]*count
            count=0
        i+=1
        #print(sum,count)
    return sum

if __name__=='__main__':
    n,m,a,b,c=readinput()
    ans=main2(n,m,a,b,c)
    print(ans)
