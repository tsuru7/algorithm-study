def readinput():
    n,k,q=map(int,input().split())
    a=[]
    for _ in range(q):
        a.append(int(input()))
    return n,k,q,a

def main(n,k,q,a):
    win=[0]*(n+1)
    for i in range(q):
        win[a[i]]+=1
    ans=[]
    #print(win)
    for i in range(1,n+1):
        point=win[i]-q+k
        if point>0:
            ans.append('Yes')
        else:
            ans.append('No')

    return ans

if __name__=='__main__':
    n,k,q,a=readinput()
    ans=main(n,k,q,a)
    for i in range(n):
        print(ans[i])
