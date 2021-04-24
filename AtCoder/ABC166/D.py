def readinput():
    x = int(input())
    return x

def main(x):
    for a in range(-118, 120):
        for b in range(-119, a):
            a2 = a*a
            b2 = b*b
            v = (a-b)*(a2*a2 + a2*a*b + a2*b2 + a*b2*b + b2*b2)
            if v == x:
                return (a, b)
            

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    x = readinput()
    ans = main(x)
    printans(ans)
