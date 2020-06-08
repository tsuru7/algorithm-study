def readinput():
    n=int(input())
    return n

def main(n):
    count=0
    for i in range(1,n+1):
        if(len(str(i))%2==1):
            count+=1
    return count

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
