def readinput():
    n,k=map(int,input().split())
    okashi=[]
    for _ in range(k):
        d=int(input())
        l=list(map(int,input().split()))
        okashi.append(l)
    return n,k,okashi

def main(n,k,okashi):
    sunuke=[0]*(n+1)
    for l in okashi:
        for su in l:
            sunuke[su]+=1
    count=0
    for i in range(n):
        if sunuke[i+1]==0:
            count+=1
    return count

if __name__=='__main__':
    n,k,okashi=readinput()
    ans=main(n,k,okashi)
    print(ans)
