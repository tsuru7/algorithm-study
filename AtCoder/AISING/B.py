def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    a.insert(0,0)
    count=0
    for i in range(1,n+1,2):
        if a[i]%2==1:
            count+=1
    return count

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
