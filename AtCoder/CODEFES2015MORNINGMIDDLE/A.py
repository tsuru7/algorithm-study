def readinput():
    n, k, m, r = map(int, input().split())
    sList = []
    for _ in range(n-1):
        sList.append(int(input()))

    return n, k, m, r, sList

def main(n, k, m, r, sList):
    if n == 1:
        return r
    
    sList.sort(reverse=True)
    sum = 0
    if k < n:
        for i in range(k):
            sum += sList[i]
        if sum >= r*k:
            return 0
        
        sum -= sList[k-1]
        if r*k - sum > m:
            return -1
        else:
            return r*k - sum
    else:
        # k == n
        for i in range(k-1):
            sum += sList[i]
        if sum >= r*k:
            return 0
        elif r*k - sum > m:
            return -1
        else:
            return r*k - sum
        

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, k, m, r, sList = readinput()
    ans = main(n, k, m, r, sList)
    printans(ans)
