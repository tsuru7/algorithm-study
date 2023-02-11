import math
import sys
INFTY=sys.maxsize

def readinput():
    n=int(input())
    return n

def main(n):
    fmin=INFTY
    m=int(math.sqrt(n))+1
    for a in range(1,m+1):
        if(n%a==0):
            b=n//a
            f=max(len(str(a)), len(str(b)))
            fmin=min(fmin,f)
    return fmin

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
