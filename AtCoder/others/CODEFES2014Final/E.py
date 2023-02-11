def readinput():
    n = int(input())
    r = list(map(int, input().split()))
    return n, r

def main(n, r):
    count = 0
    r2 = []
    r2.append(r[0])
    for i in range(1, n):
        if r[i] == r[i-1]:
            continue
        r2.append(r[i])
    l = len(r2)
    r3 = []
    r3.append(r2[0])
    for i in range(1, l-1):
        if (r2[i] - r2[i-1])*(r2[i+1]-r2[i]) < 0:
            r3.append(r2[i])
    r3.append(r2[l-1])
    if len(r3) < 3:
        ans = 0
    else:
        ans = len(r3)
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, r = readinput()
    ans = main(n, r)
    printans(ans)
