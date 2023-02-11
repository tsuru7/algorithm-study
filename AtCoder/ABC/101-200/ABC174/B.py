from math import sqrt
def readinput():
    n,d=map(int,input().split())
    xy=[]
    for _ in range(n):
        x,y=map(int,input().split())
        xy.append((x,y))
    return n,d,xy

def main(n,d,xy):
    count=0
    for x,y in xy:
        r=sqrt(x*x+y*y)
        if r<=d:
            count+=1
    return count

if __name__=='__main__':
    n,d,xy=readinput()
    ans=main(n,d,xy)
    print(ans)
