def readinput():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, a, b

def main(n, a, b):
    c = [0]*n
    for i in range(n):
        c[i] = a[i] - b[i]
    cp = 0
    for i in range(n):
        if c[i] > 0:
            cp += c[i]
    c2m = 0
    for i in range(n):
        if c[i] < 0:
            q = -c[i]//2
            c2m += q
    if c2m >= cp:
        ans = 'Yes'
    else:
        ans = 'No'
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, a,b = readinput()
    ans = main(n, a, b)
    printans(ans)
