def readinput():
    n,r=map(int,input().split())
    return n, r

def main(n, r):
    if n >= 10:
        naibu = r
    else:
        naibu = r + 100 * (10 - n)
    return naibu

if __name__=='__main__':
    n, r=readinput()
    ans=main(n, r)
    print(ans)
