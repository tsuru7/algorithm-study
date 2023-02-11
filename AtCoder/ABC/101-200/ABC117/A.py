def readinput():
    t,x=map(int,input().split())
    return t,x

def main(t,x):
    return t/x

if __name__=='__main__':
    t,x=readinput()
    ans=main(t,x)
    print(ans)
