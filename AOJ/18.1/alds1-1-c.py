import math

def readinput():
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    return n,a

def isPrime(n):
    if n==2:
        return True

    if n<=1 or n%2==0:
        return False

    m = int(math.sqrt(n))+1
    for i in range(3,m,2):
        if n % i == 0:
            return False
    return True

def getPrimes(n):
    '''n以下の素数のリストを返す'''
    p=[]
    for i in range(2,n+1):
        if isPrime(i):
            p.append(i)
    return p

def main(n,a):
    m=max(a)
    p=getPrimes(m)
    cnt=0
    for _ in a:
        if _ in p:
            cnt+=1
    return cnt

if __name__=='__main__':
    #n,a=readinput()
    #ans=main(n,a)
    n=int(input())
    cnt=0
    for i in range(n):
        x = int(input())
        if isPrime(x):
            cnt+=1
    print(cnt)
