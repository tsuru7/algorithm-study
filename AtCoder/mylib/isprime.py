import math

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

if __name__=='__main__':
    n=int(input())
    print(isPrime(n))
