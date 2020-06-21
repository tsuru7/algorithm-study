def readinput():
    h,w=list(map(int,input().split()))
    return h,w

def main(h,w):
    if (h==1 or w==1):
        return 1
    if w%2==0:
        yoko1=w//2
        yoko2=yoko1
    else:
        yoko1=w//2+1
        yoko2=yoko1-1
    if h%2==0:
        tate=h//2
        return (yoko1+yoko2)*tate
    else:
        tate=h//2
        return (yoko1+yoko2)*tate+yoko1

if __name__=='__main__':
    h,w=readinput()
    ans=main(h,w)
    print(ans)
    