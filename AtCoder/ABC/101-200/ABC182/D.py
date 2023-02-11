def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

def main(n,a):
    s = [0]*n
    t = [0]*n
    maxx = 0
    maxs = 0
    s[0] = a[0]
    t[0] = s[0]
    maxs = max(maxs, s[0])
    maxx = max(maxx, 0 + maxs)
    for i in range(1, n):
        s[i] = s[i-1] + a[i]
        t[i] = t[i-1] + s[i]
        maxs = max(maxs, s[i])
        maxx = max(maxx, t[i-1]+maxs)
    return maxx

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    print(ans)
