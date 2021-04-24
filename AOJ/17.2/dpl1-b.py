def readinput():
    n,w=list(map(int,input().split()))
    items=[]
    for _ in range(n):
        v,w=list(map(int,input().split()))
        items.append((v,w))
    return n,w,items

def main(n,w,items):
    c=[]
    for _ in range(n+1):
        l=[0]*(w+1)
        c.append(l)
    
    for i in range(1,n+1):
        item=items[i-1]
        wi=item[1]
        vi=item[0]
        for j in range(1,w+1):
            c[i][j]=max(c[i-1][w], c[i-1][w-item[1]]+item[0])


    return 0

if __name__=='__main__':
    n,w,items=readinput()
    ans=main(n,w,items)
    print(ans)
