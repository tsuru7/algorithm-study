def readinput():
    n, k = map(int, input().split())
    return n, k

def main(n, k):
    # k x 1
    ans = 6*(k-1)*(n-k)/n**3
    # k x 2
    ans += 3*(k-1)/n**3
    ans += 3*(n-k)/n**3
    # k x 3
    ans += 1/n**3
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, k = readinput()
    ans = main(n, k)
    printans(ans)

