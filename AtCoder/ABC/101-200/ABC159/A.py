def readinput():
    n,m=map(int,input().split())
    return n,m

def main(n,m):
    ans = n*(n-1)//2 + m*(m-1)//2
    return ans

if __name__=='__main__':
    n,m=readinput()
    ans=main(n,m)
    print(ans)
