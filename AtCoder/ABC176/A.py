def readinput():
    n,x,t=map(int,input().split())
    return n,x,t

def main(n,x,t):
    count=n//x
    if n%x!=0:
        count+=1
    return count*t

if __name__=='__main__':
    n,x,t=readinput()
    ans=main(n,x,t)
    print(ans)
