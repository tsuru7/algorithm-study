def readinput():
    n = int(input())
    s = list(map(int,input().split()))
    q = int(input())
    t = list(map(int,input().split()))
    return n,s,q,t

def main(n,s,q,t):
    c = 0
    for j in t:
        for i in s:
            if(i == j):
                c += 1
                break

    return c

if __name__=='__main__':
    n,s,q,t = readinput()
    ans = main(n,s,q,t)
    print(ans)
