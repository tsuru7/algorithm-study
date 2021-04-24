def readinput():
    n,q=map(int,input().split())
    s=input()
    lr=[]
    for _ in range(q):
        l,r=map(int,input().split())
        lr.append((l,r))
    return n,q,s,lr

def main(n,q,s,lr):
    count=[0]*n
    i=0
    nac=0
    while(i+1<n):
        count[i]=nac
        if s[i:i+2]=='AC':
            nac+=1
        i+=1
    count[i]=nac
    ans=[]
    for l,r in lr:
        ans.append(count[r-1]-count[l-1])
    return ans

if __name__=='__main__':
    n,q,s,lr=readinput()
    ans=main(n,q,s,lr)
    for a in ans:
        print(a)
