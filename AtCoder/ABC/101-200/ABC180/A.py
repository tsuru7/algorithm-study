def readinput():
    n,a,b=map(int,input().split())
    return n,a,b

def main(n,a,b):
    ans=n-a+b
    return ans

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    print(ans)
