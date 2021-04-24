def readinput():
    s = input()
    return s

def main(s):
    count = [0]*26
    n = len(s)
    c = ord(s[n-1]) - ord('a')
    count[c] += 1
    c = ord(s[n-2]) - ord('a')
    count[c] += 1
    ans = 0
    for i in range(n-3, -1, -1):
        c = ord(s[i]) - ord('a')
        if s[i] == s[i+1] and s[i+1] != s[i+2]:
            ans += n-i  -2 - (count[c]-1)
            count = [0]*26
            count[c] = n-i
        else:
            count[c] += 1
        # print(ans, count)
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    s = readinput()
    ans = main(s)
    printans(ans)
