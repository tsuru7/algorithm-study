def readinput():
    n=int(input())
    l=list(map(int,input().split()))
    return n,l

def main(n,l):
    lmax=max(l)
    if lmax*2<sum(l):
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    n,l=readinput()
    ans=main(n,l)
    print(ans)
