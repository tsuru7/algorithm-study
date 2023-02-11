def readinput():
    x, y, a, b, c = map(int, input().split())
    plist = list(map(int, input().split()))
    qlist = list(map(int, input().split()))
    rlist = list(map(int, input().split()))
    return x, y, a, b, c, plist, qlist, rlist

def main(x, y, a, b, c, plist, qlist, rlist):
    plist.sort(reverse=True)
    qlist.sort(reverse=True)
    rlist.sort(reverse=True)
    sum = 0
    for i in range(x):
        sum += plist[i]
    for i in range(y):
        sum += qlist[i]
    ip = x-1
    iq = y-1
    ir = 0

    if plist[ip] < qlist[iq]:
        minus = plist[ip]
        ip -= 1
    else:
        minus = qlist[iq]
        iq -= 1
    plus = rlist[0]
    ir += 1
    while plus > minus:
        # print(ip, iq, ir)
        sum += plus - minus
        if ip < 0 and iq < 0:
            break
        elif ip < 0:
            minus = qlist[iq]
            iq -= 1
        elif iq < 0:
            minus = plist[ip]
            ip -= 1
        elif plist[ip] < qlist[iq]:
            minus = plist[ip]
            ip -= 1
        else:
            minus = qlist[iq]
            iq -= 1
        if ir >= len(rlist):
            break
        plus = rlist[ir]
        ir += 1
    return sum

def printans(ans):
    print(ans)

if __name__ == '__main__':
    x, y, a, b, c, plist, qlist, rlist = readinput()
    ans = main(x, y, a, b, c, plist, qlist, rlist)
    printans(ans)
