def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def main(n, a):
    count = [0] * n
    for i in range(len(a)):
        count[a[i]] += 1
    
    if n % 2 != 0:
        if count[0] != 1:
            return 0
        for i in range(1, n):
            if i % 2 == 0:
                if count[i] != 2:
                    return 0
            else:
                if count[i] != 0:
                    return 0
        return expmod((n-1)//2)
    else:
        for i in range(n):
            if i % 2 == 0:
                if count[i] != 0:
                    return 0
            else:
                if count[i] != 2:
                    return 0
        return expmod(n//2)

def expmod(n):
    MOD = 10**9+7
    ans = 1
    for _ in range(n):
        ans = (ans * 2)%MOD
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, a = readinput()
    ans = main(n, a)
    printans(ans)
