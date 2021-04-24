import sys
INFTY = sys.maxsize

def readinput():
    h, w = map(int, input().split())
    c = []
    for _ in range(10):
        c.append(list(map(int, input().split())))
    wall = []
    for _ in range(h):
        wall.append(list(map(int, input().split())))
    
    return h, w, c, wall

def main(h, w, c, wall):
    cost = [0]*10
    cost[1] = 0
    for n in range(10):
        if n == 1:
            continue
        dp = [ [INFTY]*9 for _ in range(10) ]
        for i in range(10):
            dp[i][0] = c[n][i]
        for j in range(1, 9):
            for i in range(10):
                for k in range(10):
                    if k == 1:
                        continue
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + c[k][i])
        cost[n] = min(dp[1])
    # print(cost)
    total_cost = 0
    for i in range(h):
        for j in range(w):
            if wall[i][j] == -1:
                continue
            total_cost += cost[wall[i][j]]

    return total_cost

def printans(ans):
    print(ans)

if __name__ == '__main__':
    h, w, c, wall = readinput()
    ans = main(h, w, c, wall)
    printans(ans)

