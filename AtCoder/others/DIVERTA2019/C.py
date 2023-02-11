def readinput():
    n = int(input())
    wordList = []
    for _ in range(n):
        wordList.append(input())
    return wordList

def main(wordList):
    total = 0
    counta = 0
    countb = 0
    countba = 0
    for word in wordList:
        total += word.count('AB')
        if word[0] == 'B' and word[-1] == 'A':
            countba += 1
        elif word[0] != 'B' and word[-1] == 'A':
            counta += 1
        elif word[0] == 'B' and word[-1] != 'A':
            countb += 1
    if countba > 0:
        total += countba - 1
        if counta > 0:
            total += 1
            counta -=1
        if countb > 0:
            total += 1
            countb -= 1
    total += min(counta, countb)
    
    return total

def printans(ans):
    print(ans)

if __name__ == '__main__':
    wordList = readinput()
    ans = main(wordList)
    printans(ans)

