def readinput():
    n, a, b=map(int,input().split())
    return n,a,b

def main(n,a,b):
    r = n % (a + b)
    q = n // (a + b)
    ans = q * a + min(r, a)
    return ans

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    print(ans)
