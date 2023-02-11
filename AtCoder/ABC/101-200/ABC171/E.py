def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    allxor = a[0]
    for i in range(1,n):
        allxor = allxor ^ a[i]
    b=[0]*n
    for i in range(n):
        b[i]=allxor ^ a[i]
    
    return b

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(' '.join(map(str,ans)))
