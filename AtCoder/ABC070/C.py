from math import gcd

def readinput():
    n = int(input())
    t = []
    for _ in range(n):
        t.append(int(input()))
    return n, t

def main(n, t):
    ans = 1
    for i in range(n):
        ans = ans*t[i]//gcd(ans, t[i])
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, t = readinput()
    ans = main(n, t)
    printans(ans)
