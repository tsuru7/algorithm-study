def readinput():
    k=int(input())
    return k

def main(k):
    amari=[0]*k
    r=0
    count=0
    for i in range(1,k+1):
        count+=1
        r=(10*r+7)%k
        if r==0:
            return count
        if amari[r]>0:
            return -1
        amari[r]+=1
    return -1

if __name__=='__main__':
    k=readinput()
    ans=main(k)
    print(ans)
