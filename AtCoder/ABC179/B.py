def readinput():
    n=int(input())
    ab=[]
    for _ in range(n):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,ab

def main(n,ab):
    count=0
    for a,b in ab:
        if a==b:
            count+=1
            if count>=3:
                return 'Yes'
        else:
            count=0
    return 'No'

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    print(ans)
