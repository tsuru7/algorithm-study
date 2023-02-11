def readinput():
    a,b,c,d=map(int,input().split())
    return a,b,c,d

def main(a,b,c,d):
    xy1=a*c
    xy2=a*d
    xy3=b*c
    xy4=b*d
    return max(xy1,xy2,xy3,xy4)

if __name__=='__main__':
    a,b,c,d=readinput()
    ans=main(a,b,c,d)
    print(ans)
