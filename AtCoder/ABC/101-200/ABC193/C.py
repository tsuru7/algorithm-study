def readinput():
    n=int(input())
    return n

def main(n):
    enable = set()
    for a in range(2, 10**5+1):
        x = a * a
        if x > n:
            break
        while x <= n:
            enable.add(x)
            x *= a
    return n - len(enable)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
