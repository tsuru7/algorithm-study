def readinput():
    a = int(input())
    return a

def f(k):
    ans = 0
    s = str(k)
    for c in s:
        ans *= k
        ans += int(c)
    return ans

def main(a):
    k = 10
    while True:
        fk = f(k)
        if fk > a:
            return -1
        elif fk == a:
            return k
        else:
            k += 1

def printans(ans):
    print(ans)

if __name__ == '__main__':
    a = readinput()
    ans = main(a)
    printans(ans)
