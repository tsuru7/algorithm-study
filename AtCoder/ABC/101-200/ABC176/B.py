def readinput():
    n=input()
    return n

def main(n):
    sum=0
    j=len(n)-1
    while(j>=0):
        sum+=int(n[j])
        j-=1
    if sum%9==0:
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
