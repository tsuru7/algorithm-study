def readinput():
    n=int(input())
    return n

def main(n):
    if n==1:
        return 0
    else:
        return 1

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
