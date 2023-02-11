def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    maxk=0
    maxcount=0
    # print(max(a))
    for k in range(2,max(a)+1):
        count=0
        for m in a:
            if m%k==0:
                count+=1
        if maxcount < count:
            maxcount = count
            maxk = k
            # print(maxcount, maxk)
    return maxk

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
