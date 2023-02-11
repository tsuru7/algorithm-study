def readinput():
    n=int(input())
    c=list(input())
    return n,c

def findR(ir,c):
    i=ir
    while (i>=0 and c[i]=='W'):
        i-=1
    return i

def findW(iw,c):
    i=iw
    while(i<n and c[i]=='R'):
        i+=1
    return i

def main(n,c):
    iw=0
    iw=findW(iw,c)
    if iw==n:
        return 0
    ir=n-1
    ir=findR(ir,c)
    if ir==-1:
        return 0
    count=0
    while(iw<ir):
        #print(iw,ir)
        count+=1
        ir=findR(ir-1,c)
        iw=findW(iw+1,c)
    return count

if __name__=='__main__':
    n,c=readinput()
    ans=main(n,c)
    print(ans)
