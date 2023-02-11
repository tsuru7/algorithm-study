def readinput():
    n=int(input())
    xy=[]
    for _ in range(n):
        x,y=map(int,input().split())
        xy.append((x,y))
    return n,xy

def main(n,xy):
    gx=0
    gy=0
    for x,y in xy:
        gx+=x
        gy+=y
    gx=gx/n
    gy=gy/n
    xy1=0.0
    xy2=0.0
    xy3=0.0
    xy4=0.0
    for x,y in xy:
        x-=gx
        y-=gy
        if x >=0 and y >= 0:
            xy1=max(xy1,x+y)
        elif x <0 and y >= 0:
            xy2=max(xy2,-x+y)
        elif x < 0 and y < 0:
            xy3=max(xy3,-x-y)
        else:
            xy4=max(xy4,x-y)
    xymax=max(xy1+xy3,xy2+xy4)
    xymax=int(xymax+0.5)        


    return xymax

if __name__=='__main__':
    n,xy=readinput()
    ans=main(n,xy)
    print(ans)