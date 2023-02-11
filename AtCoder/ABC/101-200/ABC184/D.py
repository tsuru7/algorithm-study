def readinput():
    a,b,c=map(int,input().split())
    return a,b,c

memo = [ [ [-1.0]*101 for j in range(101) ] for k in range(101) ]

def f(i,j,k,a,b,c):
    if memo[i][j][k] > -0.1:
        return memo[i][j][k]

    if i<a or j<b or k<c:
        memo[i][j][k] = 0.0
        return memo[i][j][k]
    else:
        if i==a and j==b and k==c:
            memo[i][j][k] = 1.0
            return memo[i][j][k]
        else:
            memo[i][j][k] = ( f(i-1,j,k, a,b,c)*(i-1) + f(i,j-1,k, a,b,c)*(j-1) + f(i,j,k-1, a,b,c)*(k-1) )/(i+j+k-1)
            return memo[i][j][k]

def main(a,b,c):
    ans=0
    for j in range(b, 100):
        for k in range(c, 100):
            ans += (100+j+k - (a+b+c))*f(100,j,k, a,b,c)

    for i in range(a, 100):
        for k in range(c, 100):
            ans += (i+100+k - (a+b+c))*f(i,100,k, a,b,c)

    for i in range(a, 100):
        for j in range(b, 100):
            ans += (i+j+100 - (a+b+c))*f(i,j,100, a,b,c)

    return ans

if __name__=='__main__':
    a,b,c=readinput()
    ans=main(a,b,c)
    print(f(99,99,99, 98,99,99))
    print(f(99,100,99, 98,99,99))
    print(f(99,99,100, 98,99,99))
    
    print(ans)
