def readinput():
    a, b, c = map(int, input().split())
    return a, b, c

def main(a, b, c):
    if (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
        ans = 'Yes'
    else:
        ans = 'No'
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    a, b, c = readinput()
    ans = main(a, b, c)
    printans(ans)
