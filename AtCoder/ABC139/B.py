def readinput():
    a,b=list(map(int,input().split()))
    return a,b

def main(a,b):
    if b<=a:
        return 1
    x=b-a
    q=x//(a-1)
    r=x%(a-1)
    if(r==0):
        return q+1
    else:
        return q+2

def main2(a,b):
    nc=1
    ntap=0
    while(nc<b):
        ntap+=1
        nc+=a-1
    return ntap

if __name__=='__main__':
    a,b=readinput()
    ans=main2(a,b)
    print(ans,end='')
