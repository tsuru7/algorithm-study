def readinput():
    a,b,c=map(int,input().split())
    k=int(input())
    return a,b,c,k

def main(a,b,c,k):
    count=0
    while not (a<b):
        b*=2
        count+=1
    while not (b<c):
        c*=2
        count+=1
    #print(a,b,c,count)
    if count<=k:
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    a,b,c,k=readinput()
    ans=main(a,b,c,k)
    print(ans)
