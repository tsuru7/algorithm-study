def readinput():
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, m, x, y, a, b

def main(n, m, x, y, a, b):
    count = 0
    i = 0
    j = 0
    ta = a[0]
    while i < n and j < m:
        # print(i, j)
        while i < n and a[i] < ta:
            i += 1
        if i == n:
            break
        ta = a[i]
        # print(f'ta: {ta}')
        # i += 1
        tb = ta + x
        while j < m and b[j] < tb:
            j += 1
        if j == m:
            break
        count += 1
        tb = b[j]
        # print(f'tb: {tb}')
        # j += 1
        ta = tb + y
        # print(ta, tb)

    return count

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, m, x, y, a, b = readinput()
    ans = main(n, m, x, y, a, b)
    printans(ans)

