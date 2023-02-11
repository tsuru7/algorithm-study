def readinput():
    x,y,z=map(int,input().split())
    return x,y,z

def main(x,y,z):
    a=x
    b=y
    c=z
    a,b=b,a
    a,c=c,a
    return (a,b,c)

if __name__=='__main__':
    x,y,z=readinput()
    ans=main(x,y,z)
    print(' '.join(map(str,ans)))
