def readinput():
    n,m=list(map(int,input().split()))
    a=[]
    for _ in range(n):
        a.append(input())
    b=[]
    for _ in range(m):
        b.append(input())
    return n,m,a,b

def main(n,m,a,b):
    for i in range(n-m+1):
        for j in range(n-m+1):
            for k in range(m):
                #print(a[i+k][j:j+m],b[k])
                if a[i+k][j:j+m]!=b[k]:
                    break
            else:
                return 'Yes'
    return 'No'

if __name__=='__main__':
    n,m,a,b=readinput()
    ans=main(n,m,a,b)
    print(ans)
