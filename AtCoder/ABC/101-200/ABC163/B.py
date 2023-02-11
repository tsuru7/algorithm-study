def readinput():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    return n,m,a

def main(n,m,a):
    days=sum(a)
    if days>n:
        return -1
    else:
        return n-days

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    print(ans)
