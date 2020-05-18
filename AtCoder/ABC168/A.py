def readinput():
    n=int(input())
    return n

def main(m):
    n=m%10
    if (n==3):
        return 'bon'
    elif (n==0 or n==1 or n==6 or n==8):
        return 'pon'
    else:
        return 'hon'

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
