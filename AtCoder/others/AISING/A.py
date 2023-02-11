def readinput():
    l,r,d=map(int,input().split())
    return l,r,d

def main(l,r,d):
    ql=(l-1)//d
    qr=r//d
    ans=qr-ql
    return ans

if __name__=='__main__':
    l,r,d=readinput()
    ans=main(l,r,d)
    print(ans)
