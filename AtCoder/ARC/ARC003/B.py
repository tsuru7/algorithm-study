def readinput():
    n = int(input())
    wordList = []
    for _ in range(n):
        wordList.append(input())
    return n, wordList

def main(n, wordList):
    revList = []
    for word in wordList:
        revList.append(word[::-1])
    revList.sort()

    ans = []
    for word in revList:
        ans.append(word[::-1])
    
    return ans

def printans(ans):
    for word in ans:
        print(word)

if __name__ == '__main__':
    n, wordList = readinput()
    ans = main(n, wordList)
    printans(ans)
