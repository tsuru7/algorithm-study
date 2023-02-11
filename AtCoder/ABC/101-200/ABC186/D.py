def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    a_sorted=sorted(a, reverse=True)
    s=[a_sorted[0]]
    for i in range(1, n):
        s.append(s[i-1]+a_sorted[i])
    sum1=0
    for i in range(n-1):
        sum1+=a_sorted[i]*(n-(i+1))
    sum2=0
    for i in range(n-1):
        sum2+=s[n-1]-s[i]

    ans=sum1-sum2
    return ans

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
