def readinput():
    n,w=map(int,input().split())
    return n,w

def main(n,w):
    ans=n//w
    return ans

if __name__=='__main__':
    n,w=readinput()
    ans=main(n,w)
    print(ans)
