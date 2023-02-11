def readinput():
    n=int(input())
    return n

def main(n):
    ureshii = (n // 500) * 1000
    n = n % 500
    ureshii += (n // 5) * 5
    return ureshii

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
