memo = [-1]*100

def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    if memo[n] != -1:
        return memo[n]
    
    memo[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    return memo[n]

if __name__ == '__main__':
    for n in range(100):
        print(tribonacci(n))
