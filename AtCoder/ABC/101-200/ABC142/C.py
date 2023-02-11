def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    aa=[]
    for i in range(n):
        aa.append((i+1,a[i]))
    aa.sort(key=lambda x:x[1])
    b=[]
    for i in range(n):
        b.append(aa[i][0])
    return b

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(' '.join(map(str,ans)))
