def readinput():
    n=int(input())
    return n

def main(n):
    if n%2==1:
        return 0
    
    n=n//2
    count=0
    base=5
    while(base<=n):
        count+=n//base
        base*=5
    return count

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
