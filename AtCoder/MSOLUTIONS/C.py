def readinput():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    return n,k,a

def main(n,k,a):
    for i in range(n-k):
        if a[i]<a[i+k]:
            print('Yes')
        else:
            print('No')

if __name__=='__main__':
    n,k,a=readinput()
    main(n,k,a)
