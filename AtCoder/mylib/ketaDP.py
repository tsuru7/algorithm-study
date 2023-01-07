def readinput():
    n = input()
    return n

def solve(n):
    '''
    N以下の非負整数の個数を求める（自明なサンプル）
    '''
    l = len(n)
    dpsm = [0 for _ in range(l+1)]
    dpeq = [0 for _ in range(l+1)]
    dpeq[0] = 1

    for i in range(l):
        di = int(n[i])
        # smaller -> smaller (d: [0..9])
        # i 桁目で smaller であれば、i+1 桁目は自由に選べる
        for d in range(10):
            dpsm[i+1] += dpsm[i]
        # equal -> smaller (d: [0..di-1])
        # i 桁目で equal のときは、i+1 桁目が 0..(di-1) であれば smaller
        for d in range(di):
            dpsm[i+1] += dpeq[i]
        # equal -> equal (d: di)
        # i 桁目で equal のとき、i+1 桁目が di であれば equal
        dpeq[i+1] += dpeq[i]
    return dpsm[l] + dpeq[l]

def printans(ans):
    print(ans)
    return

if __name__ == '__main__':
    n = readinput()
    ans = solve(n)
    printans(ans)
