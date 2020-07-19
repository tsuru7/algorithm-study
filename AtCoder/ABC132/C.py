def readinput():
    n=int(input())
    d=list(map(int,input().split()))
    return n,d

def main(n,d):
    ds=sorted(d)
    m=n//2
    if ds[m-1]==ds[m]:
        return 0
    else:
        return ds[m]-ds[m-1]

if __name__=='__main__':
    n,d=readinput()
    ans=main(n,d)
    print(ans)
