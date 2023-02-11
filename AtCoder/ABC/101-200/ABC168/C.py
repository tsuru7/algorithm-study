from math import pi,cos,sin,sqrt

def readinput():
    a,b,h,m=list(map(int,input().split()))
    return a,b,h,m

def main(a,b,h,m):
    tmin=h*60+m
    u=tmin*2*pi/(12*60)
    t=m*2*pi/60
    dist=sqrt(
        (a*cos(u)-b*cos(t))**2
        +(a*sin(u)-b*sin(t))**2
        )
    return dist

if __name__=='__main__':
    a,b,h,m=readinput()
    ans=main(a,b,h,m)
    print('{:.10f}'.format(ans))

