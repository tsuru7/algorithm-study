def readinput():
    n = int(input())
    wordList = input().split()
    return n, wordList

def trans(c):
    if c in 'bc':
        return '1'
    elif c in 'dw':
        return '2'
    elif c in 'tj':
        return '3'
    elif c in 'fq':
        return '4'
    elif c in 'lv':
        return '5'
    elif c in 'sx':
        return '6'
    elif c in 'pm':
        return '7'
    elif c in 'hk':
        return '8'
    elif c in 'ng':
        return '9'
    elif c in 'zr':
        return '0'
    else:
        return ''
        
def main(n, wordList):
    ans = []
    for word in wordList:
        xword = ''
        word = word.lower()
        # print(word)
        for c in word:
            xword += trans(c)
        if xword != '':
            ans.append(xword)
    return ans

def printans(ans):
    print(' '.join(ans))

if __name__ == '__main__':
    n, wordList = readinput()
    ans = main(n, wordList)
    printans(ans)
