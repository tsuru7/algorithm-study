from math import gcd
def readinput():
    k=int(input())
    return k

def main(k):
    memo=[]
    for _j in range(k+1):
        memo.append([0 for _i in range(k+1)])
    sum=0
    for a in range(1,k+1):
        for b in range(1,k+1):
            if memo[a][b]!=0:
                temp=memo[a][b]
            else:
                temp=gcd(a,b)
                memo[a][b]=temp
                memo[b][a]=temp
            for c in range(1,k+1):
                if memo[temp][c]!=0:
                    sum+=memo[temp][c]
                else:
                    temp2=gcd(temp,c)
                    memo[temp][c]=temp2
                    memo[c][temp]=temp2
                    sum+=temp2
    return sum

if __name__=='__main__':
    k=readinput()
    ans=main(k)
    print(ans)
