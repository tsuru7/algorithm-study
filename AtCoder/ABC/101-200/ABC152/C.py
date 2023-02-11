def readinput():
    n=int(input())
    p=list(map(int,input().split()))
    return n,p

def main(n,p):
    count=0
    pmin=p[0]
    for i in range(n):
        pmin=min(p[i],pmin)
        if pmin>=p[i]:
            count+=1
    return count

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    print(ans)
