def readinput():
    x, y, w = input().split()
    x = int(x)
    y = int(y)
    cmap = []
    for _ in range(9):
        cmap.append(input())
    return x, y, w, cmap

def flipx(w):
    if 'R' in w:
        w = w.replace('R', 'L')
    elif 'L' in w:
        w = w.replace('L', 'R')
    return w

def flipy(w):
    if 'U' in w:
        w = w.replace('U', 'D')
    elif 'D' in w:
        w = w.replace('D', 'U')
    return w

def next(x, y, w):
    if 'R' in w:
        if x < 9:
            x += 1
        else:
            x -= 1
            w = flipx(w)

    elif 'L' in w:
        if x > 1:
            x -= 1
        else:
            x += 1
            w = flipx(w)

    if 'U' in w:
        if y > 1:
            y -= 1
        else:
            y += 1
            w = flipy(w)
    elif 'D' in w:
        if y < 9:
            y += 1
        else:
            y -= 1
            w = flipy(w)
    return x, y, w

def main(x, y, w, cmap):
    ans = ''
    for _ in range(4):
        # print(x, y, w)
        ans = ans + cmap[y-1][x-1]
        x, y, w = next(x, y, w)

    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    x, y, w, cmap = readinput()
    ans = main(x, y, w, cmap)
    printans(ans)
