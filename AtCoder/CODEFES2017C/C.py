def readinput():
    s = input()
    return s

def main(s):
    l = 0
    r = len(s) - 1
    count = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == 'x':
            l += 1
            count += 1
        elif s[r] == 'x':
            r -= 1
            count += 1
        else:
            return -1
    return count

def printans(ans):
    print(ans)

if __name__ == '__main__':
    s = readinput()
    ans = main(s)
    printans(ans)
