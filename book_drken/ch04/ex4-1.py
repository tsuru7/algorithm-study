def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

if __name__ == '__main__':
    for n in range(100):
        print(tribonacci(n))
