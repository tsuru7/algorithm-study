def readinput():
    n=int(input())
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    return n,a,b,c,d,e

def main(n,a,b,c,d,e):
    r=min(a,b,c,d,e)
    m=n//r
    if n%r!=0:
        m+=1
    return m+4

if __name__=='__main__':
    n,a,b,c,d,e=readinput()
    ans=main(n,a,b,c,d,e)
    print(ans)
