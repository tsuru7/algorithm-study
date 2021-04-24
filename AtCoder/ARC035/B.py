

def readinput():
    n = int(input())
    t = []
    for _ in range(n):
        t.append(int(input()))
    return n, t

def main(n, t):
    MOD=10**9+7
    f = [0] * (10001)
    f[0] = 1
    for i in range(1, 10001):
        f[i] = (f[i-1]*i)%MOD
    t = sorted(t)
    # print(t)
    total = 0
    penalty = 0
    pattern = 1
    count = 0
    prev = 0
    for i in range(n):
        if prev == t[i]:
            count += 1
            # print(t[i], count)
        else:
            pattern = (pattern * f[count+1]) % MOD
            # print(t[i], pattern, count, f[count+1])
            count = 0
        penalty = penalty + t[i]
        total = total + penalty
        prev = t[i]
    else:
        pattern = (pattern * f[count+1]) % MOD
    return total, pattern


def printans(ans):
    print(ans[0])
    print(ans[1])

if __name__ == '__main__':
    n, t = readinput()
    ans = main(n, t)
    printans(ans)


