def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    hist=[0]*(10**5+1)
    for i in range(n):
        hist[a[i]]+=1
    
    max3=0
    for i in range(10**5-1):
        max3=max(max3,hist[i]+hist[i+1]+hist[i+2])
    return max3

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)

