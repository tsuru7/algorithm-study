def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    tgt=1
    count=0
    for i in range(n):
        if a[i]==tgt:
            tgt+=1
        else:
            count+=1
    if count==n:
        return -1
    else: 
        return count

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
