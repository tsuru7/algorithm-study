def readinput():
    h, w, k = map(int, input().split())
    smap = []
    for _ in range(h):
        smap.append(input())
    return h, w, k, smap

def main(h, w, k, smap):
    ans = [[0 for j in range(w)] for i in range(h)]
    p = 1
    i = 0
    line = smap[i]
    while not '#' in line:
        i += 1
        line = smap[i]
    count = 0
    for j, c in enumerate(line):
        if c == '.':
            ans[i][j] = p
        else:
            count += 1
            if count > 1:
                p += 1
            ans[i][j] = p
    if i > 0:
        for ii in range(i):
            for j in range(w):
                ans[ii][j] = ans[i][j]
    for ii in range(i+1, h):
        line = smap[ii]
        if not '#' in line:
            for j in range(w):
                ans[ii][j] = ans[ii-1][j]
        else:
            p += 1
            count = 0
            for j, c in enumerate(line):
                if c == '.':
                    ans[ii][j] = p
                else:
                    count += 1
                    if count > 1:
                        p += 1
                    ans[ii][j] = p

    return ans

def printans(ans):
    for a in ans:
        print(' '.join(map(str, a)))

if __name__ == '__main__':
    h, w, k, smap = readinput()
    ans = main(h, w, k, smap)
    printans(ans)
