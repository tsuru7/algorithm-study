def readinput():
    n=int(input())
    return n

def getKeta(n):
    m=n-1
    base=0
    keta=1
    base+=26**keta
    while(m>=base):
        keta+=1
        base+=26**keta
    return keta

def naming(keta,n):
    alph='abcdefghijklmnopqrstuvwxyz'
    geta=26*(26**(keta-1)-1)//25
    m=n-geta-1
    name=''
    for _ in range(keta):
        r=m%26
        m=m//26
        name=alph[r]+name
    return name

def main(n):
    keta=getKeta(n)
    #print(keta)
    
    name=naming(keta,n)

    return name



if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
