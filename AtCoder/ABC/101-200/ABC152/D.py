def readinput():
    n=int(input())
    return n

def main(n):
    count = [ [0]*10 for _ in range(10)]
    m = 1
    while m <= n:
        head = int(str(m)[0])
        tail = int(str(m)[-1])
        count[head][tail] += 1
        m += 1
    
    ans=0
    for i in range(1,10):
        for j in range(1,10):
            ans += count[i][j] * count[j][i]
    return ans

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
