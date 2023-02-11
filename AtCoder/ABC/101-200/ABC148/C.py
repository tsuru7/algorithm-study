from math import gcd

def readinput():
    a,b=map(int,input().split())
    return a,b

def main(a,b):
    return a*b//gcd(a,b)

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    print(ans)
