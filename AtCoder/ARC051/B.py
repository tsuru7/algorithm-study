def readinput():
    k = int(input())
    return k

def eucleides(a, b):
    if b == 0:
        return 0
    return 1 + eucleides(b, a%b)


def main(k):
    n = 1
    m = 1
    a = m
    b = 0
    for _ in range(k+1):
        a, b = n*a+b, a
    ans = (a, b)
    # if eucleides(a, b) != k:
    #     print('NE', 'eucleides({}, {}): {}'.format(a, b, eucleides(a,b)))
    # else:
    #     print('EQ')
    return ans

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    k = readinput()
    ans = main(k)
    printans(ans)
