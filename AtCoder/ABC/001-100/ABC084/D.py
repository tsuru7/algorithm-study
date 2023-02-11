def readinput():
    q = int(input())
    lr = []
    for _ in range(q):
        lr.append(list(map(int, input().split())))
    return lr

def findPrimes():
    primes = [1]*(10**5+1)
    primes[0] = 0
    primes[1] = 0
    primes[2] = 1
    for i in range(4, 10**5+1, 2):
        primes[i] = 0
    for i in range(3, 10**5+1, 2):
        for j in range(i*2, 10**5+1, i):
            primes[j] = 0
    return primes

def findPrimes2(primes):
    primes2 = [0] * (10**5+1)
    for i in range(3, 10**5+1, 2):
        if primes[i] == 1:
            j = (i+1)//2
            if primes[j] == 1:
                primes2[i] = 1
    return primes2

def main(lr):
    primes = findPrimes()
    primes2 = findPrimes2(primes)
    counts = [0]*(10**5+1)
    count = 0
    for i in range(10**5+1):
        if primes2[i] == 1:
            count += 1
        counts[i] = count
    ans = []
    for l, r in lr:
        ans.append(counts[r] - counts[l-1])
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__ == '__main__':
    lr = readinput()
    ans = main(lr)
    printans(ans)
