def readinput():
    n = int(input())
    return n

def main(n):
    for i in range(1,10):
        for j in range(1,i+1):
            if i*j == n:
                return 'Yes'
    return 'No'

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
