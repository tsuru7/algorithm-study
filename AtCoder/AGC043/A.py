import sys
INFTY = sys.maxsize

def readinput():
    h, w = map(int, input().split())
    smap = []
    for _ in range(h):
        smap.append(input())
    return h, w, smap

def main(h, w, smap):
    dp = [ [INFTY for j in range(w)] for i in range(h)]
    dp[0][0] = 0 if smap[0][0] == '.' else 1
    for y in range(1, h):
        if smap[y-1][0] == '.' and smap[y][0] == '#':
            dp[y][0] = min(dp[y][0], dp[y-1][0] + 1)
        else:
            dp[y][0] = min(dp[y][0], dp[y-1][0])
    for x in range(1, w):
        for y in range(h):
            # 右に移動する場合
            if smap[y][x-1] == '.' and smap[y][x] == '#':
                dp[y][x] = min(dp[y][x], dp[y][x-1]+1)
            else:
                dp[y][x] = min(dp[y][x], dp[y][x-1])
            # 下に移動する場合
            if smap[y-1][x] == '.' and smap[y][x] == '#':
                dp[y][x] = min(dp[y][x], dp[y-1][x] + 1)
            else:
                dp[y][x] = min(dp[y][x], dp[y-1][x])
    return dp[h-1][w-1]

def printans(ans):
    print(ans)

if __name__ == '__main__':
    h, w, smap = readinput()
    ans = main(h, w, smap)
    printans(ans)
