def readinput():
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    return n, xy

def main(n, xy):
    if n == 1 or n == 2:
        return 1

    # n > 2のときを考える
    xy.sort()
    # print(xy)
    maxcount = 0
    for i in range(n-1):
        xi, yi = xy[i]
        for j in range(i+1, n):
            xj, yj = xy[j]
            p = xj - xi
            q = yj - yi
            count = 0
            for k1 in range(n-1):
                for k2 in range(k1+1, n):
                    a, b = xy[k1]
                    c, d = xy[k2]
                    if c-a == p and d-b == q:
                        count += 1
            maxcount = max(maxcount, count)
    return n - maxcount

from collections import Counter
def main2(n, xy):
    if n == 1 or n == 2:
        return 1
        
    edges = []
    for i in range(n):
        xi, yi = xy[i]
        for j in range(n):
            xj, yj = xy[j]
            if i == j:
                continue
            edges.append((xj-xi, yj-yi))
    counter = Counter(edges)
    maxcount = max(counter.values())
    return n - maxcount

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, xy = readinput()
    ans = main2(n, xy)
    printans(ans)
