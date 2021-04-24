def readinput():
    n=int(input())
    l=list(map(int,input().split()))
    return n,l

def main(n,l):
    count=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i]==l[j] or l[i]==l[k] or l[j]==l[k]:
                    continue
                lmax=max(l[i],l[j],l[k])
                sonota=l[i]+l[j]+l[k]-lmax
                if sonota>lmax:
                    #print(i,j,k)
                    count+=1
    return count

if __name__=='__main__':
    n,l=readinput()
    ans=main(n,l)
    print(ans)
