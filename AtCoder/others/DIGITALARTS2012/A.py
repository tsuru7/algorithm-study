s=input()
n=int(input())
tList = []
for _ in range(n):
    tList.append(input())

wordList = s.split()
for i, word in enumerate(wordList):
    for ngword in tList:
        if len(word) != len(ngword):
            continue
        for j, c in enumerate(ngword):
            if c == '*':
                continue
            if c != word[j]:
                break
        else:
            wordList[i] = '*'*len(word)
print(' '.join(wordList))
