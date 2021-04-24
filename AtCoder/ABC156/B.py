def readinput():
    n,k=map(int,input().split())
    return n,k

def main(n,k):
    keta = 0
    while n > 0:
        keta += 1
        r = n % k
        n = n // k
    return keta

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    print(ans)
