def readinput():
    n,m,x,y=map(int,input().split())
    xx=list(map(int,input().split()))
    yy=list(map(int,input().split()))
    return n,m,x,y,xx,yy

def main(n,m,x,y,xx,yy):
    xx.append(x)
    yy.append(y)
    xx.sort()
    yy.sort()
    if xx[-1]<yy[0]:
        return 'No War'
    else:
        return 'War'

if __name__=='__main__':
    n,m,x,y,xx,yy=readinput()
    ans=main(n,m,x,y,xx,yy)
    print(ans)
