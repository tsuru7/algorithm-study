def readinput():
    n,k=map(int,input().split())
    return n,k

def main(n,k):
    # a,b,cがkの倍数の場合
    m = n//k
    count=m*m*m
    # kが偶数のとき
    # a,b,cがkの倍数+k/2の場合
    if k%2==0:
        m=(n+k//2)//k
        count+=m*m*m
    return count

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    print(ans)
