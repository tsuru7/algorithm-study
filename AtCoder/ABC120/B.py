def readinput():
    a,b,k=list(map(int,input().split()))
    return a,b,k

def main(a,b,k):
    ans=0
    count=0
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            count+=1
            if count==k:
                return i


if __name__=='__main__':
    a,b,k=readinput()
    ans=main(a,b,k)
    print(ans)
