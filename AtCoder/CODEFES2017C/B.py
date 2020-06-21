def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    evena=[False]*n
    for i in range(n):
        if a[i]%2==0:
            evena[i]=True
    count=0
    for i in range(3**n):
        #print(i)
        neven=0
        for bit in range(n):
            mask=3**bit
            if (i//mask)%3 == 0:
                #print('mask0')
                if evena[bit]==False:
                    neven+=1
            elif (i//mask)%3 == 1:
                #print('mask1')
                if evena[bit]==True:
                    neven+=1
            elif (i//mask)%3 == 2:
                #print('mask2')
                if evena[bit]==False:
                    neven+=1
            #else:
                #print('????')
        if neven>0:
            count+=1
    return count

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
  
        