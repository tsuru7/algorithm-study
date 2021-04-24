def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    genkin=1000
    kabu=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            # 売り
            genkin+=kabu*a[i]
            kabu=0
        elif a[i]<a[i+1]:
            # 買い
            kabu+=genkin//a[i]
            genkin=genkin%a[i]
    if kabu>0:
        genkin+=kabu*a[n-1]
    return genkin

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
