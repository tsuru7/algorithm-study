def readinput():
    n = int(input())
    s = input()
    return n, s

def main(n, s):
    left = 0
    right = 0
    for c in s:
        if c == '(':
            left += 1
        elif c == ')':
            if left > 0:
                left -= 1
            else:
                right += 1
    ans = '('*right + s + ')'*left
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, s = readinput()
    ans = main(n, s)
    printans(ans)
