def readinput():
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    return a,b,c,d

def main(a,b,c,d):
    ans=a*d-b*c
    return ans

if __name__=='__main__':
    a,b,c,d=readinput()
    ans=main(a,b,c,d)
    print(ans)
