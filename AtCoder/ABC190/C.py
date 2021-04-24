def readinput():
    n,m=map(int,input().split())
    ab = []
    for _ in range(m):
        a,b=map(int,input().split())
        ab.append((a,b))
    k = int(input())
    cd = []
    for _ in range(k):
        c, d=map(int, input().split())
        cd.append((c,d))
    return n,m,ab,k,cd

def main(n,m,ab,k,cd):
    maxcount=0
    for i in range(2**k):
        dishes = [-1]*(n+1)
        bit = 1
        for j in range(k):
            c, d = cd[j]
            if i & bit == bit:
                dishes[c] = 1
            else:
                dishes[d] = 1
            bit *= 2
        count=0
        for j in range(m):
            a, b = ab[j]
            if dishes[a] == 1 and dishes[b] == 1:
                count += 1
        maxcount = max(maxcount, count)
    return maxcount

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,ab,k,cd=readinput()
    ans=main(n,m,ab,k,cd)
    printans(ans)
