def readinput():
    a, b, c = map(int, input().split())
    return a, b, c

def main(a, b, c):
    if c > a+b and (c-a-b)**2 - 4*a*b > 0:
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

