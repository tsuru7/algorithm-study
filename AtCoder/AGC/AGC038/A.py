def readinput():
    h, w, a, b = map(int, input().split())
    return h, w, a, b

def main(h, w, a, b):
    ans = []
    for i in range(b):
        ans.append('0'*a+'1'*(w-a))
    for i in range(b, h):
        ans.append('1'*a+'0'*(w-a))
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__ == '__main__':
    h, w, a, b = readinput()
    ans = main(h, w, a, b)
    printans(ans)
