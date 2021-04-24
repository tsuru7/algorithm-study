from collections import Counter

def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def main(n, a):
    cumsum = [0]*n
    cumsum[0] = a[0]
    for i in range(1, n):
        cumsum[i] = cumsum[i-1]+a[i]
    # print(cumsum)
    counter = Counter(cumsum)
    # print(counter)
    ans = 0
    for k, v in counter.items():
        if k == 0:
            v += 1
        ans += v*(v-1)//2
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, a = readinput()
    ans = main(n, a)
    printans(ans)
