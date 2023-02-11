def readinput():
    n, m = map(int, input().split())
    xy = []
    for _ in range(m):
        xy.append(list(map(int, input().split())))
    
    return n, m, xy

def main(n, m, xy):
    nums = [1]*(n+1)
    poss = [0]*(n+1)
    poss[1] = 1
    for x, y in xy:
        if poss[x] == 1:
            if nums[x] > 1:
                nums[x] -= 1
                nums[y] += 1
                poss[y] = 1
            else:
                nums[x] -= 1
                nums[y] += 1
                poss[x] = 0
                poss[y] = 1
        else:
            nums[x] -= 1
            nums[y] += 1
    count = 0
    for i in range(1, n+1):
        if poss[i] > 0:
            count += 1
    return count

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, m, xy = readinput()
    ans = main(n, m, xy)
    printans(ans)
