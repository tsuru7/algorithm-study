def readinput():
    n = int(input())
    a = []
    for i in range(n):
        a.append((int(input()), i))
    return n, a

def main(n, a):
    a = sorted(a, key=lambda x: x[0])
    b = [0] * n
    v = 0
    b[a[0][1]] = v
    for i in range(1, n):
        if a[i-1][0] < a[i][0]:
            v += 1
        b[a[i][1]] = v
    return b

def printans(ans):
    for bi in ans:
        print(bi)

if __name__ == '__main__':
    n, a = readinput()
    ans = main(n, a)
    printans(ans)
