def readinput():
    h, w = map(int, input().split())
    smap = []
    for _ in range(h):
        smap.append(input())
    return h, w, smap

def main(h, w, smap):
    ans = 'possible'
    tmap = [ ['#']*w for _ in range(h) ]
    # smapに白が存在するための必要条件
    for i in range(h):
        for j in range(w):
            if smap[i][j] == '.':
                if i > 0:
                    if j > 0:
                        tmap[i-1][j-1] = '.'
                    tmap[i-1][j] = '.'
                    if j < w-1:
                        tmap[i-1][j+1] = '.'
                if j > 0:
                    tmap[i][j-1] = '.'
                tmap[i][j] = '.'
                if j < w-1:
                    tmap[i][j+1] = '.'

                if i < h-1:
                    if j > 0:
                        tmap[i+1][j-1] = '.'
                    tmap[i+1][j] = '.'
                    if j < w-1:
                        tmap[i+1][j+1] = '.'
    # smapに黒が存在するための十分条件
    for i in range(h):
        for j in range(w):
            if smap[i][j] == '#':
                if isBpossible(i, j, h, w, tmap):
                    continue
                else:
                    return 'impossible', tmap

    return ans, tmap

def isBpossible(i, j, h, w, tmap):
    if i > 0:
        if j > 0 and tmap[i-1][j-1] == '#':
            return True
        if tmap[i-1][j] == '#':
            return True
        if j < w-1 and tmap[i-1][j+1] == '#':
            return True
    if j > 0 and tmap[i][j-1] == '#':
        return True
    if tmap[i][j] == '#':
        return True
    if j < w-1 and tmap[i][j+1] == '#':
        return True
    if i < h-1:
        if j > 0 and tmap[i+1][j-1] == '#':
            return True
        if tmap[i+1][j] == '#':
            return True
        if j < w-1 and tmap[i+1][j+1] == '#':
            return True
    return False

    

def printans(ans, tmap):
    print(ans)
    if ans == 'possible':
        for i in range(h):
            print(''.join(tmap[i]))

if __name__ == '__main__':
    h, w, smap = readinput()
    ans, tmap = main(h, w, smap)
    printans(ans, tmap)

