def readinput():
    n, m = map(int, input().split())
    return n, m

def main(n, m):
    i = 1
    ans = 1
    while i*i <= m:
        q, r = divmod(m, i)
        if r == 0 and q >= n:
            ans = max(ans, i)
        if r == 0 and i >= n:
            ans = max(ans, q)
        i += 1
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, m = readinput()
    ans = main(n, m)
    printans(ans)
