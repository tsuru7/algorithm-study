def readinput():
    n=int(input())
    p=list(map(int,input().split()))
    return n,p

def main(n,p):
    deta = [0]*(200000+1)
    imin=0
    ans=[]
    for i in range(n):
        deta[p[i]]=1
        while deta[imin]==1:
            imin+=1
        ans.append(imin)
    return ans

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    for a in ans:
        print(a)
