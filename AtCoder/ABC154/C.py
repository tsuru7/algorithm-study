def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    a.sort()
    for i in range(n-1):
        if a[i]==a[i+1]:
            return 'NO'
    return 'YES'

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
