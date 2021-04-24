def readinput():
    x = int(input())
    return x

def main(x):
    t = 0
    sum = 0
    while sum < x:
        t += 1
        sum += t
    return t

def printans(ans):
    print(ans)

if __name__ == '__main__':
    x = readinput()
    ans = main(x)
    printans(ans)
