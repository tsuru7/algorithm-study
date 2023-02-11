def readinput():
    a,b,x=list(map(int,input().split()))
    return a,b,x

def main(a,b,x):
    ans = b//x - (a-1)//x
    return ans

if __name__=='__main__':
    a,b,x=readinput()
    ans=main(a,b,x)
    print(ans)
