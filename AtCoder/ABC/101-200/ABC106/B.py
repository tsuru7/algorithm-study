def readinput():
    n=int(input())
    return n

def main(n):
    count=0
    for i in range(3,n+1,2):
        nc=0
        for j in range(1,i+1):
            if(i%j==0):
                nc+=1
        if nc==8:
            count+=1
    return count

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
