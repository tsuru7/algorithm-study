from math import sqrt

def readinput():
    x, y, r=map(float, input().split())
    return x, y, r

def dist2(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

def det(r, x, n):
    return r**2 - (n-x)**2

def divmod_r(x, d):
    if x > 0:
        return divmod(x, d)
    else:
        q, r = divmod(-x, d)
        return (-q, -r)

def main(x, y, r):
    # 第1象限に平行移動
    dist = min(int(round(x-r)), int(round(y-r)))
    if dist < 0:
        x += dist + 10
        y += dist + 10
    # スケールをk=10000倍にする
    k = 10000
    x = int(round(x * k))
    y = int(round(y * k))
    r = int(round(r * k))
    x0 = ((x - r - k)//k) * k
    x1 = ((x + r + k)//k) * k
    n = x0
    count = 0
    while n <= x1:
        d = det(r, x, n)
        if d >= 0:
            yl, res = divmod(int(round(y - sqrt(d))), k)
            if res > 0:
                yl += 1
            yr = int(round(y + sqrt(d)))//k
            count += (yr - yl) + 1
            # print(n, yl, yr)
        n += k

    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    x, y, r=readinput()
    ans=main(x, y, r)
    printans(ans)
