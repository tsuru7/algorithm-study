def readinput():
    n=int(input())
    return n

def main(n):
    MOD=10**9+7
    ans=pow(10,n,MOD)-pow(9,n,MOD)-pow(9,n,MOD)+pow(8,n,MOD)
    ans=(ans+MOD)%MOD
    return ans

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
