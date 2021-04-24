from math import gcd
def readinput():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    return n,m,a

def lcm(a,b):
    return a*b//gcd(a,b)

def main(n,m,a):
    #s=set(a)
    #print(s)
    x=a[0]//2
    for i in range(1,n):
        x=lcm(x,a[i]//2)
    #print(x)
    gusubai=False
    kisubai=False
    for i in range(n):
        if x%a[i]!=0:
            gusubai=True
        else:
            kisubai=True
    
    y=m//x
    #print(y,x,m)
    if gusubai and not kisubai:
        ans=y//2+y%2
    elif gusubai and kisubai:
        ans=0
    else:
        ans=y
    return ans

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    print(ans)
