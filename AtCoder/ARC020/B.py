import sys
INFTY = sys.maxsize

def readinput():
    n, c = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))
    return n, c, a

def main(n, c, a):
    count_odd = [0] * 10
    count_even = [0] * 10
    for i in range(n):
        if i % 2 == 1:
            count_odd[a[i]-1] += 1
        else:
            count_even[a[i]-1] += 1
    minchange = INFTY
    for i in range(10):
        for j in range(10):
            if i == j:
                continue
            if n % 2 == 0:
                change_odd = n // 2 - count_odd[i]
                change_even = n // 2 - count_even[j]
            else:
                change_odd = n // 2 + 1 - count_odd[i]
                change_even = n // 2 - count_even[j]
            minchange = min(minchange, change_odd + change_even)
    return minchange * c

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, c, a = readinput()
    ans = main(n, c, a)
    printans(ans)
