from collections import Counter

def readinput():
    n = int(input())
    s = input()
    return n, s


def main(n, s):
    MOD = 10**9 + 7

    count = 1
    counter = Counter(s)
    for value in counter.values():
        # print(key, counter[key])
        count = (count * (value+1)) % MOD 

    return (count-1) % MOD

def printans(ans):
    print(ans)

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)

    n, s = readinput()
    ans = main(n, s)
    printans(ans)
