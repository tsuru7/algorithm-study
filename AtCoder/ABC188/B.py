def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    return n,a,b

def main(n,a,b):
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    if sum == 0:
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    print(ans)
