from math import sqrt
def readinput():
    n=int(input())
    return n

def main(n):
    m=int(sqrt(n))+1
    count=0
    for a in range(1,m+1):
        if a*a < n:
            count+=1
        else:
            break
    
    for a in range(1,m+1):
        for b in range(a+1,n+1):
            if a*b < n:
                count+=2
            else:
                break
    return count

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
