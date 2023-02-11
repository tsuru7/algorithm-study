def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    allxor=0
    for i in range(n):
        allxor = allxor ^ a[i]
    if allxor == 0:
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
