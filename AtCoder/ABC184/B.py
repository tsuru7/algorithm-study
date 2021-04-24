def readinput():
    n,x=map(int,input().split())
    s=input()
    return n,x,s

def main(n,x,s):
    ans=x
    for c in s:
        if c == 'o':
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    return ans

if __name__=='__main__':
    n,x,s=readinput()
    ans=main(n,x,s)
    print(ans)
