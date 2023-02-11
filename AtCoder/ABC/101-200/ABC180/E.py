def readinput():
    n=int(input())
    xs=[]
    ys=[]
    zs=[]
    for _ in range(n):
        x,y,z=map(int,input().split())
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return n,xs,ys,zs

def main(n,xs,ys,zs):
    minx=min(xs)
    maxx=max(xs)
    miny=min(ys)
    maxy=max(ys)
    minz=min(zs)
    maxz=max(zs)
    cost = (maxx - minx)*2 + (maxy - miny)*2 +(maxz - minz) 
    return cost

if __name__=='__main__':
    n,xs,ys,zs=readinput()
    ans=main(n,xs,ys,zs)
    print(ans)