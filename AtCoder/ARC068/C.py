def readinput():
    x = int(input())
    return x

def main(x):
    q = x // 11
    r = x % 11
    count = 2 * q
    if 1 <= r and r and r <= 6:
        count += 1
    elif 7 <= r and r <=10:
        count += 2
    return count

def printans(ans):
    print(ans)

if __name__ == '__main__':
    x = readinput()
    ans = main(x)
    printans(ans)
