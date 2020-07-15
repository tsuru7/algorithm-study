def readinput():
    n=int(input())
    return n

def main(n):
    amari=n%1000
    if amari==0:
        return 0
    else:
        return 1000-amari

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
