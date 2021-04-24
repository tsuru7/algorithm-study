from bisect import bisect_left, bisect_right

def readinput():
    n,m=map(int,input().split())
    h=list(map(int,input().split()))
    w=list(map(int,input().split()))
    return n,m,h,w

def main(n,m,h,w):
    sum=0
    for i in range(n-1):
        for j in range(i+1,n):
            sum += abs(h[i]-h[j])
    h = sorted(h)
    w = sorted(w)

    for wi in w:
        hi = bisect_left(h, wi)
        if hi == 0:
            hi = 1
        hj = bisect_right(h, w)
        abs(h[hi]-wi), abs(h[hj]-wi)

    ans=0
    return ans

if __name__=='__main__':
    n,m,h,w=readinput()
    ans=main(n,m,h,w)
    print(ans)