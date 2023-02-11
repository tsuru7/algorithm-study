class Eratosthenes:
    def __init__(self, n):
        self.n = n
        self.primes = [True for _ in range(n+1)]
        self.primes[0] = False
        self.primes[1] = False
        i = 2
        x = i
        while x + i <= n:
            x += i
            self.primes[x] = False
        for i in range(3, n+1, 2):
            if i*i > n:
                break
            if not self.primes[i]:
                continue
            x = i
            while x + i <= n:
                x += i
                self.primes[x] = False
        return
    
    def isPrime(self, x):
        return self.primes[x]
    
    def getPrimes(self):
        return self.primes

    def getPrimeList(self):
        primeList = []
        for i, flg in enumerate(self.primes):
            if flg:
                primeList.append(i)
        return primeList


