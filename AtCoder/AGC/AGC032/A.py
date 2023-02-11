def readinput():
    n = int(input())
    b = list(map(int, input().split()))
    return n, b

def main(n, b):
    a = []
    while len(b) > 0:
        for i in range(len(b)-1, -1, -1):
            if b[i] == i+1:
                a.insert(0, b.pop(i))
                break
        else:
            return [-1]
    return a

def printans(ans):
    for a in ans:
        print(a)

if __name__ == '__main__':
    n, b = readinput()
    ans = main(n, b)
    printans(ans)

