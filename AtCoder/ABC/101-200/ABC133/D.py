def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    #a.insert(0,0)
    s=[0]*(2*n+1)
    sign=1
    for i in range(2*n):
        j=i%n
        s[i+1]=s[i]+sign*a[j]
        sign=sign*(-1)

    ans=[]
    sign=1
    for i in range(n):
        ans.append( sign*(s[n+i]-s[i]) )
        sign=sign*(-1)
    return ans

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(' '.join(map(str,ans)))
