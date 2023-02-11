def readinput():
    s = input()
    return s

def main(s):
    nums = [0]*26
    for c in s:
        idx = ord(c) - ord('a')
        nums[idx] += 1
    
    m = 0
    for i in range(26):
        if nums[i] %2 != 0:
            m += 1
    # print(f'm={m}')
    
    l = len(s)

    if m == 0:
        x = l
    else:
        x = 1
        k = (l - m)//2
        x += (k//m)*2
    return x

def printans(ans):
    print(ans)

if __name__ == '__main__':
    s = readinput()
    ans = main(s)
    printans(ans)
