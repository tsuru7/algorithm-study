def readinput():
    n,a,b=list(map(int,input().split()))
    s=[]
    for _ in range(n):
        s.append(int(input()))
    return n,a,b,s

def main(n,a,b,s):
    avg=0
    maxs=-1
    mins=10**9+1
    for ss in s:
        maxs=max(maxs,ss)
        mins=min(mins,ss)
        avg+=ss
    avg=avg/n
    if maxs==mins:
        print(-1)
    else:
        p=b/(maxs-mins)
        q=a-avg*p
        print(p,q)


if __name__=='__main__':
    n,a,b,s=readinput()
    main(n,a,b,s)


