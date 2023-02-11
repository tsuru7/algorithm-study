import sys
INFTY = sys.maxsize

def readinput():
    n = int(input())
    w = []
    for _ in range(n):
        w.append(int(input()))
    return n, w

def main(n, w):
    yama = [INFTY] * n
    for box in w:
        i = 0
        while True:
            if box <= yama[i]:
                yama[i] = box
                break
            else:
                i += 1
    ans = 0
    for i in range(n):
        if yama[i] == INFTY:
            break
        ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, w = readinput()
    ans = main(n, w)
    printans(ans)
