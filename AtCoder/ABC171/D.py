def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    bcList=[]
    for _ in range(q):
        bcList.append(list(map(int,input().split())))
    return n,a,q,bcList

def main(n,a,q,bcList):
    hist=[0]*(10**5+1)
    for v in a:
        hist[v]+=1

    sum=0
    for i in range(1,10**5+1):
        sum+=i*hist[i]

    for b,c in bcList:
        sum=sum+hist[b]*(c-b)
        hist[c]+=hist[b]
        hist[b]=0
        print(sum)


if __name__=='__main__':
    n,a,q,bcList=readinput()
    main(n,a,q,bcList)

