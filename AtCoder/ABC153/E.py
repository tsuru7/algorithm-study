import sys
INFTY = sys.maxsize // 2

def readinput():
    h, n = map(int, input().split())
    ab = []
    for _ in range(n):
        ab.append(list(map(int, input().split())))
    return n, h, ab

def main(n, h, ab):
    dp = [ [INFTY]*(h+1) for _ in range(n+1)]
    # i番目までの魔法を使ってjのダメージを与える時の魔力の最小値
    # hのダメージを与える時に注意
    # オーバーキルしても良いからh以上のダメージを与えるようにする
    dp[0][0] = 0
    for i in range(1, n+1):
        a, b = ab[i-1]
        for j in range(h+1):
            # 魔法 i を使わないとき
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            # 魔法 i を使うとき
            if j >= a:
                dp[i][j] = min(dp[i][j], dp[i][j-a]+b)
        if h % a > 0:
            dp[i][h] = min(dp[i][h], dp[i][h-(h%a)]+b)


        # print(dp[i])
    return dp[n][h]

def printdp(dp):
    for l in dp:
        print(l)
    print()

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, h, ab = readinput()
    ans = main(n, h, ab)
    printans(ans)

