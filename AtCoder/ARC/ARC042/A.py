def readinput():
    n,m=list(map(int,input().split()))
    a=[]
    for _ in range(m):
        a.append(int(input()))
    return n,m,a

def main(n,m,a):
    order=[[0,0]]
    for i in range(1,n+1):
        order.append([i,n-i+1])
    for i in range(m):
        order[a[i]][1]=n+i+1
    s=sorted(order, reverse=True, key=lambda x: x[1])
    for i in range(n):
        print(s[i][0])

if __name__=='__main__':
    n,m,a=readinput()
    main(n,m,a)

