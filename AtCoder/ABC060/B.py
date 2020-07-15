def readinput():
    a,b,c=map(int,input().split())
    return a,b,c

def main(a,b,c):
    amari=[0]*b
    looped=False
    x=a
    while(not looped):
        r=x%b
        if r==c:
            return 'YES'
        if amari[r]>0:
            looped=True
            return 'NO'
        else:
            amari[r]+=1
        x=x+a

if __name__=='__main__':
    a,b,c=readinput()
    ans=main(a,b,c)
    print(ans)
