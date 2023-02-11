def readinput():
    n=int(input())
    return n

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

def main(n):
    divisors = myDivisors(n*2)
    count = 0
    i = 0
    j = len(divisors) - 1
    while i < len(divisors):
        x = divisors[i]
        if (divisors[j] - x - 1) % 2 == 0:
            count += 1
        i += 1
        j -= 1
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
