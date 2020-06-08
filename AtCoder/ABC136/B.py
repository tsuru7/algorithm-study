def readinput():
    n=int(input())
    return n

def main(n):
    if 1<=n and n<=9:
        return n
    elif 10<=n and n<=99:
        return 9
    elif 100<=n and n<=999:
        return 9+(n-99)
    elif 1000<=n and n<=9999:
        return 9+900
    elif 10000<=n and n<=99999:
        return 9+900+(n-9999)
    elif 100000==n:
        return 9+900+90000
    return 0

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
