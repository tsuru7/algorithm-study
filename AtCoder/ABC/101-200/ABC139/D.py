def readinput():
    n=int(input())
    return n

def main(n):
    return n*(n-1)//2

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
