def readinput():
    n=int(input())
    a=[0]
    for _ in range(n):
        a.append(int(input()))
    return n,a

def main(n,a):
    button=[0]*(n+1)
    button[1]=1
    i=1
    count=0
    while(True):
        i=a[i]
        count+=1
        if i==2:
            return count
        if button[i]>0:
            return -1
        button[i]+=1

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
