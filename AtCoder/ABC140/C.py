def readinput():
    n=int(input())
    b=list(map(int,input().split()))
    return n,b

def main(n,b):
    sum=b[0]
    for i in range(1,n-1):
        sum+=min(b[i-1],b[i])
    sum+=b[n-2]
    return sum

if __name__=='__main__':
    n,b=readinput()
    ans=main(n,b)
    print(ans)
