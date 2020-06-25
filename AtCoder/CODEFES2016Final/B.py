from math import sqrt

def readinput():
    n=int(input())
    return n

def main(n):
    k=int((-1+sqrt(1+8*n))/2)
    while(k*(k+1)//2<n):
        k+=1
    dif=k*(k+1)//2 - n
    for i in range(1,dif):
        print(i)
    for i in range(dif+1,k+1):
        print(i)

if __name__=='__main__':
    n=readinput()
    main(n)
