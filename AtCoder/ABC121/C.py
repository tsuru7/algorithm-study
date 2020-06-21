def readinput():
    n,m=list(map(int,input().split()))
    #a=[]
    #b=[]
    ab=[]
    for _ in range(n):
        aa,bb=list(map(int,input().split()))
        #a.append(aa)
        #b.append(bb)
        ab.append((aa,bb))

    return n,m,ab

def main(n,m,ab):
    ab2=sorted(ab)
    price=0
    bought=0
    for i in range(n):
        a,b=ab2[i]
        if(bought+b>=m):
            buy=m-bought
            price+=a*buy
            return price
        bought+=b
        price+=a*b

if __name__=='__main__':
    n,m,ab=readinput()
    ans=main(n,m,ab)
    print(ans)

    