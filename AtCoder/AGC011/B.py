def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def main(n, a):
    a.sort()
    cumsum = [0]*n
    cumsum[0] = a[0]
    count = 1
    for i in range(1, n):
        cumsum[i] = cumsum[i-1]+a[i]
        if a[i] <= 2*cumsum[i-1]:
            count += 1
        else:
            count = 1
    return count

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, a = readinput()
    ans = main(n, a)
    printans(ans)
