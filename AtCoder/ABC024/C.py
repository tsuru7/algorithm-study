def readinput():
    n, d, k = map(int, input().split())
    lr = []
    for _ in range(d):
        lr.append(list(map(int, input().split())))
    st = []
    for _ in range(k):
        st.append(list(map(int, input().split())))
    return n, d, k, lr, st

def main(n, d, k, lr, st):
    ans = []
    for s, t in st:
        pos = s
        if s < t:
            goRight = True
        else:
            goRight = False
        days = 0
        for l, r in lr:
            days += 1
            if l <= pos and pos <= r and goRight:
                if t <= r:
                    ans.append(days)
                    break
                else:
                    pos = r
            elif l <= pos and pos <= r and not goRight:
                if l <= t:
                    ans.append(days)
                    break
                else:
                    pos = l
    return ans
                

def printans(ans):
    for a in ans:
        print(a)

if __name__ == '__main__':
    n, d, k, lr, st = readinput()
    ans = main(n, d, k, lr, st)
    printans(ans)

