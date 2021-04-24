def readinput():
    n, s, d=map(int,input().split())
    xy = []
    for _ in range(n):
        xy.append(list(map(int,input().split())))
    return n, s, d, xy

def main(n, s, d, xy):
    for x, y in xy:
        if x >= s:
            continue
        if y <= d:
            continue
        return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n, s, d, xy=readinput()
    ans=main(n, s, d, xy)
    printans(ans)
