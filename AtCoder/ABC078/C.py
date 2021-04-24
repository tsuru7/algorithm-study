n, m = map(int, input().split())
T = 1900 * m + 100 * (n - m)
print(T * 2**m)
