def readinput():
    n,k=list(map(int,input().split()))
    abList=[]
    for _ in range(n):
        a,b=list(map(int,input().split()))
        abList.append((a,b))
    return n,k,abList

def main(n,k,abList):
    hist=[0]*(10**5+1)
    for a,b in abList:
        hist[a]+=b
    sum=0
    for i in range(1,10**5+1):
        sum+=hist[i]
        if sum>=k:
            return i
    else:
        return 0

if __name__=='__main__':
    n,k,abList=readinput()
    ans=main(n,k,abList)
    print(ans)
