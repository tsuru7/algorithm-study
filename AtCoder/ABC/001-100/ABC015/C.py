def readinput():
    n, k = map(int, input().split())
    tmat = []
    for _ in range(n):
        tmat.append(list(map(int, input().split())))
    return n, k, tmat

def main(n, k, tmat):
    for x in range(k**n):
        sum = 0
        i = 0
        while i < n:
            j = x % k
            sum ^= tmat[i][j]
            x = x // k
            i += 1
        if sum == 0:
            return 'Found'
    return 'Nothing'

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, k, tmat = readinput()
    ans = main(n, k, tmat)
    printans(ans)
