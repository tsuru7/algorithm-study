def readinput():
    n=int(input())
    return n

def main(n):
    if n%2==0:
        return 0.5
    else:
        return (n//2+1)/n


if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
