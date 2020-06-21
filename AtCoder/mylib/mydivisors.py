import math
def myDivisors(n):
    '''nの約数を列挙する

    戻り値: divisors (set)
    '''

    divisors=set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
        i += 1
    return sorted(divisors)

if __name__=='__main__':
    n=int(input())
    ans=myDivisors(n)
    print(ans)
