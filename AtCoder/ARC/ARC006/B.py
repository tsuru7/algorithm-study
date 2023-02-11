def readinput():
    n,l=list(map(int,input().split()))
    tateList=[[]]
    for i in range(1,n+1):
        tate=[i]*l
        tateList.append(tate)
    for j in range(l):
        yoko=input()
        i=0
        for i in range(1,n):
            ii=2*(i-1)+1
            if yoko[ii]=='-':
                tateList[i][j]=i+1
                tateList[i+1][j]=i
    a=input()
    atari=a.find('o')//2+1
    return n,l,tateList,atari

def main(n,l,tateList,atari):
    current=atari
    j=l-1
    while(j>=0):
        current=tateList[current][j]
        j-=1
    return current

if __name__=='__main__':
    n,l,tateList,atari=readinput()
    #print(tateList,atari)
    ans=main(n,l,tateList,atari)
    print(ans)

    
