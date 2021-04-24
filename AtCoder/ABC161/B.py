def readinput():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    return n,m,a

def main(n,m,a):
    a.sort(reverse=True)
    total=sum(a)
    if a[m-1]*(4*m)<total:
        return 'No'
    else:
        return 'Yes'

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    print(ans)
