def readinput():
    n = int(input())
    return n

def main(n):
    if n % 2 == 1:
        return 'Black'
    else:
        return 'White'

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
