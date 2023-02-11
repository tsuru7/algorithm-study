def readinput():
    w,h,x,y=map(int,input().split())
    return w,h,x,y

def main(w,h,x,y):
    s=w*h/2
    center=0
    if 2*x==w and 2*y==h:
        center=1
    return s,center

if __name__=='__main__':
    w,h,x,y=readinput()
    ans=main(w,h,x,y)
    print(ans[0],ans[1])
