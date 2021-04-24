def readinput():
    n=int(input())
    ab=[]
    for _ in range(n):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,ab

def main(n,ab):
    ans=0
    for a, b in ab:
        ans += (a + b)*(b - a + 1)//2
    return ans

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    print(ans)
