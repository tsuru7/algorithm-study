def readinput():
    na,nb=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    return na,nb,a,b

def main(na,nb,a,b):
    seta=set(a)
    setb=set(b)
    uab=seta | setb
    iab=seta & setb
    ans=len(iab)/len(uab)
    return ans

if __name__=='__main__':
    na,nb,a,b=readinput()
    ans=main(na,nb,a,b)
    print(ans)
