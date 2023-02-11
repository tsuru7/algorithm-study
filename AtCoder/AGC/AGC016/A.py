def readinput():
    s = input()
    return s

def main(s):
    mincounts = 100
    for i in range(26):
        c = chr(ord('a')+i)
        l = 0
        maxcounts = 0
        for j in range(len(s)):
            l += 1
            if s[j] == c:
                maxcounts = max(maxcounts, l-1)
                l = 0
        else:
            remains = l
        maxcounts = max(maxcounts, remains)
        mincounts = min(mincounts, maxcounts)
    return mincounts

def printans(ans):
    print(ans)

if __name__ == '__main__':
    s = readinput()
    ans = main(s)
    printans(ans)
