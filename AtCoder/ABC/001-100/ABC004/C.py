def readinput():
    n = int(input())
    return n

def main(n):
    results = []
    s = '123456'
    results.append(s)
    for i in range(6):
        for j in range(5):
            if i == 5 and j == 4:
                continue
            t = ''
            for k in range(6):
                if k == j:
                    t += s[k+1]
                elif k == j+1:
                    t += s[k-1]
                else:
                    t += s[k]
            results.append(t)
            s = t
    # print(results)
    r = n % 30
    return results[r]

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n = readinput()
    ans = main(n)
    printans(ans)
