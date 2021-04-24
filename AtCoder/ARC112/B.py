def readinput():
    b, c = map(int, input().split())
    return b, c

def main(b, c):
    if b > 0:
        if c == 1:
            count = 2
        elif c >= 2:
            count = 2  # 自分自身と-1倍
            count += min(b, c//2)
            count += min(b-1, (c-1)//2)
            maxb = b + (c-2)//2
            count += maxb - b
            minb = -b - (c-1)//2
            count += -b - minb
    elif b == 0:
        if c == 1:
            count = 1
        else:
            minb = - (c//2)
            maxb = (c-1)//2
            count = maxb - minb + 1
    else:
        if c == 1:
            count = 2
        else:
            count = 2 # 自分自身と-1倍
            count += min(-b, (c-1)//2)
            count += min(-b-1, (c-2)//2)
            maxb = -b + (c-1)//2
            count += maxb - (-b)
            minb = b - (c//2)
            count += b - minb

    return count

def printans(ans):
    print(ans)

if __name__ == '__main__':
    b, c = readinput()
    ans = main(b, c)
    printans(ans)

