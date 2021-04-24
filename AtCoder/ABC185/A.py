def readinput():
    a=list(map(int,input().split()))
    return a

def main(a):
    ans=min(a)
    return ans

if __name__=='__main__':
    a=readinput()
    ans=main(a)
    print(ans)
