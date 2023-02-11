def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, a, b

def main(n, a, b):
    c = [0]*n
    defeat = 0
    count = 0
    for i in range(n):
        c[i] = a[i] - b[i]
        if c[i] < 0:
            defeat += -c[i]
            count += 1
    c.sort(reverse=True)
    for i in range(n):
        # print(f'i: {i}, defeat: {defeat}')
        if defeat <= 0:
            return i + count
        defeat -= c[i]
    else:
        return -1

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, a, b = readinput()
    ans = main(n, a, b)
    printans(ans)
