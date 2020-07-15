def readinput():
    n,k=map(int,input().split())
    return n,k

def main(n,k):
    ans=k
    for i in range(1,n):
        ans=ans*(k-1)
        if ans >2**31-1:
            return 2**31-1
    return ans

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    print(ans)
