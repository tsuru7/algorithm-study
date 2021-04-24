import sys
INFTY = sys.maxsize

def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def main(n, a):
    cumsum = [0]*n
    cumsum[0] = a[0]
    for i in range(1, n):
        cumsum[i] = cumsum[i-1] + a[i]
    minabs = INFTY
    for i in range(0, n-1):
        x = cumsum[i]
        y = cumsum[n-1] - cumsum[i]
        minabs = min(minabs, abs(x-y))
    return minabs

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, a = readinput()
    ans = main(n, a)
    printans(ans)
