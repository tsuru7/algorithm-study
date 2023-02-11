def readinput():
    n=int(input())
    ab=[]
    for _ in range(n):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,ab

def main(n,ab):
    ab.sort(key=lambda x:x[1], reverse=True)
    t=ab[0][1]
    for i in range(n):
        if ab[i][1]<t:
            t=ab[i][1]
        t=t-ab[i][0]
    if t>=0:
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    print(ans)
