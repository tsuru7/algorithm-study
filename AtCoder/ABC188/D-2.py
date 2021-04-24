def readinput():
    n, c = map(int, input().split())
    kakin = dict()
    for _ in range(n):
        a, b, ci = map(int, input().split())
        if a in kakin.keys():
            kakin[a] += ci
        else:
            kakin[a] = ci
        if b+1 in kakin.keys():
            kakin[b+1] -= ci
        else:
            kakin[b+1] = -ci
    return c, kakin

def main(c, kakin):
    # print(c, kakin)
    kakin_sorted = sorted(kakin.items(), key=lambda x: x[0])
    # print(kakin_sorted)

    total_cost = 0
    prevday = kakin_sorted[0][0]
    cost = kakin_sorted[0][1]
    for i in range(1, len(kakin_sorted)):
        today = kakin_sorted[i][0]
        # print(f'day(morning): {today}, cost: {cost}')
        if cost < c:
            total_cost += cost * (today - prevday)
        else:
            total_cost += c * (today - prevday)
        # print(f'total_cost: {total_cost}')
        cost += kakin_sorted[i][1]
        prevday = today
    return total_cost

def printans(ans):
    print(ans)

if __name__ == '__main__':
    c, kakin = readinput()
    ans = main(c, kakin)
    printans(ans)
