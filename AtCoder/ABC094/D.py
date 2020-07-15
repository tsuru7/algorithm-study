from bisect import bisect_left, bisect_right
import sys
INFTY=sys.maxsize

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    # order=[]
    # for i in range(n):
    #     order.append([a[i],i])
    s=sorted(a)
    ai=s[n-1]

    aj0=ai/2
    j=bisect_right(s, aj0)-1
    #print(s,aj0,j) 
    aj=s[j]
    if aj==aj0:
        return ai,aj

    if j+1<n:
        aj1=s[j]
        aj2=s[j+1]
        if aj0-aj1<=aj2-aj0:
            aj=aj1
        else:
            aj=aj2
    return ai,aj


if __name__=='__main__':
    n,a=readinput()
    i,j=main(n,a)
    print(i,j)
