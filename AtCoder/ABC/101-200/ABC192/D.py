def readinput():
    x = int(input())
    m = int(input())
    return x,m

def get_value(x, n):
    s = str(x)
    ans = 0
    base = n
    for c in s:
        ans *= base
        ans += int(c)
    return ans

def main(x,m):
    s = str(x)
    if len(s) == 1:
        if x <= m:
            return 1
        else:
            return 0
    d = 0
    for c in s:
        if d < int(c):
            d = int(c)

    # if m < get_value(x, d+1):
    #     return 0
    
    l = d
    r = 10**19
    while r - l > 1:
        mid = (l+r)//2
        v_mid = get_value(x, mid)
        # print('l, r, v_mid: ', l, r, v_mid)
        if m < v_mid:
            r = mid
        else:
            l = mid
        # print('l, r: ', l, r)
        
    
    ans = l - d
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,m=readinput()
    ans=main(x,m)
    printans(ans)
