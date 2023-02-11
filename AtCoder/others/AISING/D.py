def readinput():
    n=int(input())
    x=input()
    return n,x


def popcount(n):
    binn=bin(n)
    return binn.count('1')

def f(n):
    #print(n)
    if n==0:
        return 0
    else:
        m=n%popcount(n)
        return f(m)+1

def main(n,x):
    intx=int(x,2)
    ans=[]
    b=1
    for i in range(n):
        y=intx^b
        ans.append(f(y))
        b=b*2
    return reversed(ans)

def makeFtbl(n):
    Ftbl=[0]*(n+1)
    Ftbl[1]=1
    Ftbl[2]=1
    for i in range(3,n+1):
        m=i%popcount(i)
        Ftbl[i]=Ftbl[m]+1
    return Ftbl

def main2(n,x):
    Ftbl=makeFtbl(n)
    intx=int(x,2)
    return [0]

popinit=False
popdict={}
def popcounts(x):
    global popinit
    global popdict
    '''文字列xに含まれる'1'の数を返す
    '''
    if x.find('0b')!=-1:
        x=x[2:]
    if not popinit:
        popdict[x]=x.count('1')
        for i in range(len(x)):
            ibit=int(x[i],2)
            jbit=ibit^1
            y=x[:i]+str(jbit)+x[i+1:]
            if ibit==1:
                popdict[y]=popdict[x]-1
            else:
                popdict[y]=popdict[x]+1
        popinit=True
    if x in popdict.keys():
        return popdict[x]
    else:
        return x.count('1')

def fs(n):
    #print(n)
    if n==0:
        return 0
    else:
        binn=bin(n)[2:]
        m=n%popcounts(binn)
        return fs(m)+1

def main3(n,x):
    intx=int(x,2)
    ans=[]
    b=1
    for i in range(n):
        y=intx^b
        ans.append(fs(y))
        b=b*2
    return reversed(ans)

if __name__=='__main__':
    n,x=readinput()
    ans=main3(n,x)
    for a in ans:
        print(a)